# -*- coding: utf-8 -*-

import sys
from unicode_tr import unicode_tr
import grpc

import zemberek_grpc.language_id_pb2 as z_langid
import zemberek_grpc.language_id_pb2_grpc as z_langid_g
import zemberek_grpc.normalization_pb2 as z_normalization
import zemberek_grpc.normalization_pb2_grpc as z_normalization_g
import zemberek_grpc.preprocess_pb2 as z_preprocess
import zemberek_grpc.preprocess_pb2_grpc as z_preprocess_g
import zemberek_grpc.morphology_pb2 as z_morphology
import zemberek_grpc.morphology_pb2_grpc as z_morphology_g


channel = grpc.insecure_channel('localhost:6789')

langid_stub = z_langid_g.LanguageIdServiceStub(channel)
normalization_stub = z_normalization_g.NormalizationServiceStub(channel)
preprocess_stub = z_preprocess_g.PreprocessingServiceStub(channel)
morphology_stub = z_morphology_g.MorphologyServiceStub(channel)

def find_lang_id(i):
    response = langid_stub.Detect(z_langid.LanguageIdRequest(input=i))
    return response.langId

def tokenize(i):
    response = preprocess_stub.Tokenize(z_preprocess.TokenizationRequest(input=i))
    return response.tokens

def normalize(i):
    response = normalization_stub.Normalize(z_normalization.NormalizationRequest(input=i))
    return response

def analyze(i):
    response = morphology_stub.AnalyzeSentence(z_morphology.SentenceAnalysisRequest(input=i))
    return response

def fix_decode(text):
    """Pass decode."""
    if sys.version_info < (3, 0):
        return text.decode('utf-8')
    else:
        return text

def run():
    lang_detect_input = 'merhaba dünya'
    lang_id = find_lang_id(lang_detect_input)
    print("Language of [" + fix_decode(lang_detect_input) + "] is: " + lang_id)

    print("")
    tokenization_input = 'Merhaba dünya!'
    print('Tokens for input : ' + fix_decode(tokenization_input))
    tokens = tokenize(tokenization_input)
    for t in tokens:
        print(t.token + ':' + t.type)

    print("")
    normalization_input = 'yenİlendiğinden beri memnuniyetim amcıĞı  azaldı. Ilık daha geniş olan hücrelerinden çıkan pamukçuklar tene yapıŞıyor. Sitedeki fiyatlar gayet iyi'
    norm_low_case_str = unicode_tr(normalization_input).lower()
    print('Normalization result for input : ' + norm_low_case_str)
    # print('Normalization result for input : ' + fix_decode(norm_low_case_str))
    n_response = normalize(fix_decode(norm_low_case_str))
    if n_response.normalized_input:
        print(n_response.normalized_input)
    else:
        print('Problem normalizing input : ' + n_response.error)

    # print("")
    # analysis_input = 'Kavanozun kapağını açamadım.'
    # print('Analysis result for input : ' + fix_decode(analysis_input))
    # analysis_result = analyze(analysis_input)
    # for a in analysis_result.results:
    #     best = a.best
    #     lemmas = ""
    #     for l in best.lemmas:
    #       lemmas = lemmas + " " + l
    #     print("Word = " + a.token + ", Lemmas = " + lemmas + ", POS = [" + best.pos + "], Full Analysis = {" + best.analysis + "}")


if __name__ == '__main__':
    run()