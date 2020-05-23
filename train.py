
#导入库
from model.model import *
from model.pre_process import *
import torch
#读入数据
dataClass = Corpus('./data/qingyun.tsv', maxSentenceWordsNum=25)
#指定模型和一些超参
model = Seq2Seq(dataClass, featureSize=256, hiddenSize=256,
                attnType='L', attnMethod='general',
                encoderNumLayers=5, decoderNumLayers=3,
                encoderBidirectional=True,
                device=torch.device('cpu:0'))
#训练
model.train(batchSize=2048, epoch=200)
#保存模型
model.save('modelL-2048-200.pkl')