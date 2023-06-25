from transformers import RobertaTokenizer, RobertaConfig, RobertaModel
from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn as nn

#用 AutoModel.from_pretrained() 从hugging face上下载模型
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base",trust_remote_code=True,revision="main")    # "microsoft/codebert-base"
model = AutoTokenizer.from_pretrained("neulab/codebert-python")

#用 PreTrainedModel.save_pretrained() 保存模型到本地指定位置
tokenizer.save_pretrained("codebert-base",trust_remote_code=True,revision="main")
model.save_pretrained("codebert-python",trust_remote_code=True,revision="main")

# 后续本地指定文件中如果还缺少什么东西，就再从hugging face上下载，然后直接放入本地我呢见加中即可