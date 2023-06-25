

# Code Search

## Task Description
Given a natural language as the input, the task aims to find the most semantically related code from a collection of candidate codes. 

![image](https://github.com/Katherine0214/CodeSearch/edit/main/CodeSearchExample.png)

## Data Preprocess

Different from the setting of [CodeSearchNet](husain2019codesearchnet), the answer of each query is retrieved from the whole development and testing code corpus instead of 1,000 candidate codes. Besides, we observe that some queries contain content unrelated to the code, such as a link ``http://..." that refers to external resources.  Therefore, we filter following examples to improve the quality of the dataset. 

- Remove comments in the code

- Remove examples that codes cannot be parsed into an abstract syntax tree.

- Remove examples that #tokens of documents is < 3 or >256

- Remove examples that documents contain special tokens (e.g. <img ...> or https:...)

- Remove examples that documents are not English.

Data statistic about the cleaned dataset for code document generation is shown in this Table.

| PL         | Training |  Dev   |  Test  | Candidates code |
| :--------- | :------: | :----: | :----: | :-------------: |
| Python     | 251,820  | 13,914 | 14,918 |     43,827      |
| PHP        | 241,241  | 12,982 | 14,014 |     52,660      |
| Go         | 167,288  | 7,325  | 8,122  |     28,120      |
| Java       | 164,923  | 5,183  | 10,955 |     40,347      |
| JavaScript |  58,025  | 3,885  | 3,291  |     13,981      |
| Ruby       |  24,927  | 1,400  | 1,261  |      4,360      |

You can download and preprocess data using the following command.
```shell
unzip dataset.zip
cd dataset
bash run.sh 
cd ..
```

dataset.zip and codebert-python/pytorch_model.bin can be found here: https://drive.google.com/file/d/1ZO-xVIzGcNE6Gz9DEg2z5mIbBv4Ft1cK/view.


## Demo 

- demo/demo.py
  
  能实实现Task Description中描述内容的脚本（原始，无排序）

- demo/demo_topN.py
  
  能实实现Task Description中描述内容的脚本（有排序，能给出Top N的代码及相应分数）
  
- demo/download_offline.py
  
  将HuggingFace上的预训练模型下载到本地，然后从本地加载模型

## Results 
![image](https://github.com/Katherine0214/CodeSearch/edit/main/Example1.png)

![image](https://github.com/Katherine0214/CodeSearch/edit/main/Example2.png)


