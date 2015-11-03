data = csv2cell('./AllDataCSV/All.csv','fromfile');
id = data(:,1);
unq_id = unique(id);
num_features = length(unq_id);
num_dat = 4904;
alldata = cell(num_dat+1,num_features);
alldata(1,:) = unq_id;
for i = 1:num_dat
    tmp_dat = csv2cell(['./AllDataCSV/' num2str(i) '.csv'],'fromfile');
    for j = 1:num_features
        tst = strcmp( unq_id(j), tmp_dat(:,1) );
        if all( tst == 0 )
            alldata(i+1,j) = {'NaN'};
        else
            tmp = tmp_dat(tst,2);
            alldata(i+1,j) = tmp(1);
        end
    end
    disp(i)
end
    
cell2csv('AllData.csv',alldata,',',2010,'.')