echo Run Tesseract for Training.. 

tesseract.exe my.test.exp0.tif my.test.exp0 nobatch box.train 


echo Compute the Character Set.. 

unicharset_extractor.exe my.test.exp0.box 

mftraining -F font_properties -U unicharset -O my.unicharset my.test.exp0.tr 



echo Clustering.. 

cntraining.exe my.test.exp0.tr 



echo Rename Files.. 

rename normproto my.normproto 

rename inttemp my.inttemp 

rename pffmtable my.pffmtable 

rename shapetable my.shapetable  



echo Create Tessdata.. 

combine_tessdata.exe my. 



echo. & pause
