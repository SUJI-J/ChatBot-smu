from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel

p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin', userdic='../utils/user_dic.tsv')
intent = IntentModel(model_name='../models/intent/intent_model.h5', proprocess=p)

query = "스마트정보통신공학과 학과사무실 번호 알려줘"
predict = intent.predict_class(query)
predict_label = intent.labels[predict]
print("질문 : ", query)
print("의도 예측 클래스 : ", predict)
print("의도 예측 레이블 : ", predict_label)
print()
query = "한누리관1층 시설 알려줘"
predict = intent.predict_class(query)
predict_label = intent.labels[predict]
print("질문 : ", query)
print("의도 예측 클래스 : ", predict)
print("의도 예측 레이블 : ", predict_label)
