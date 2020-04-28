echo Run Tesseract for Training.. 
tesseract.exe chi.myself.exp1.tif chi.myself.exp1 nobatch box.train 

echo Compute the Character Set.. 
unicharset_extractor.exe chi.myself.exp1.box 
mftraining -F font_properties -U unicharset -O my.unicharset chi.myself.exp1.tr 


echo Clustering.. 
cntraining.exe chi.myself.exp1.tr 

echo Rename Files.. 
rename normproto my.normproto 
rename inttemp my.inttemp 
rename pffmtable my.pffmtable 
rename shapetable my.shapetable  

echo Create Tessdata.. 
combine_tessdata.exe my. 

echo. & pause