# CHAGNGELOG

## edit code

A: 調整架構
B: 改變coding style
C: 修改code，使可跑
D: Debug

### June 10, 2020
+ C-1: src/LiviaNET_Config.ini 修改資料集路徑、資料集為nifti
+ C-2: src/LiviaNet/Modules/IO/loadData.py 加入nifti threshold，解決讀nifti檔案問題

### June 12, 2020
+ C-3: 修改資料集為BraTS，label 3+1
+ C-4: src/LiviaNet/startTraining.py 

### June 13, 2020
+ D-1: src/LiviaNET_Config.ini, BraTS的label是4+1, MR shape皆為[240,240,155]
+ D-2: MICCAI Atlas資料集的MR shape會變動[256,256,261:320]，所以要使用這個資料集，需要preprocessing。relate issue: [josedolz
/
LiviaNET #4](https://github.com/josedolz/LiviaNET/issues/4 )、[josedolz
/
LiviaNET #5](https://github.com/josedolz/LiviaNET/issues/5 )
+ A-1: delete src/LiviaNet/Modules/General/__init__.pyc
+ A-2: add Dataset/nifti_label_info.py 用來看nifti data的label num, total label, shape
+ C-5: src/LiviaNet/startTraining.py, 紀錄subepoch的cost作為loss圖

### June 14, 2020
+ A-3: src/LiviaNet/startTraining.py 修改numberOfSubEpochs，讓其以指定sub epoch數目進行每個epoch