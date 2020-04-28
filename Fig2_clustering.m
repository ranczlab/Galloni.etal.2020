load('Fig2a.mat')

all = [V1;V2];

%% Elbow plot
subplot(4,3,1)
distances = zeros(1,10);
for klist=1:10
    [idx,C,sumd,D] = kmeans(all,klist,'Replicates',50);
    distances(klist) = sum(sumd);
end
plot(distances)
ylabel('sum of point-to-centroid distances')
xlabel('no. of kmeans clusters')
set(gca,'FontSize',15)
xlim([1,10])

%% Silhouette plot
for k = 2:6
    subplot(4,3,k)
    [idx,C] = kmeans(all,k,'Replicates',50);
    [s,h] = silhouette(all,idx,'Euclidean');
    set(gca,'FontSize',15)
end

%% Raincloud plots

subplot(4,3,7:9)
    %Plot raincloud
    [h,u] = raincloud_plot('X',all,'box_on',1,'box_dodge',1,'band_width',15,'bxfacecl',[1,1,1],'cloud_edge_col', [0.8 0.8 0.8],'point_size',50,'color',[0.7,0.7,0.7]);  
    xlim([0,250])
    hold on
    
    %add lines separating the clusters
    [idx,C] = kmeans(all,2,'Replicates',50);
    cluster1 = all(find(idx==1));
    cluster2 = all(find(idx==2));
    
    if C(1) < C(2)
        line = (max(cluster1) + min(cluster2))/2;
    else
        line = (max(cluster2) + min(cluster1))/2;
    end
    plot([line,line],[-1,1],'k--','LineWidth',2)

    set(gca,'FontSize',20)
    set(gca,'ytick',[])
    txt1 = strcat('k=2');
    text(150,0.008,txt1,'FontSize',20)    
    
subplot(4,3,10:12)
    %Plot raincloud
    [h,u] = raincloud_plot('X',all,'box_on',1,'box_dodge',1,'band_width',15,'bxfacecl',[1,1,1],'cloud_edge_col', [0.8 0.8 0.8],'point_size',50,'color',[0.7,0.7,0.7]);  
    xlim([0,250])
    xlabel('max ADP integral (ms*mV)','FontSize',40)
    hold on 
    
    %add lines separating the clusters
    [idx,C] = kmeans(all,3,'Replicates',50);
    cluster1 = all(find(idx==1));
    cluster2 = all(find(idx==2));
    cluster3 = all(find(idx==3));
    
    if C(1)<C(2) && C(2)<C(3)
        line1 = (max(cluster1) + min(cluster2))/2;
        line2 = (max(cluster2) + min(cluster3))/2;
    elseif C(2)<C(1) && C(1)<C(3)
        line1 = (max(cluster2) + min(cluster1))/2;
        line2 = (max(cluster1) + min(cluster3))/2;
    elseif C(1)<C(3) && C(3)<C(2)
        line1 = (max(cluster1) + min(cluster3))/2;
        line2 = (max(cluster3) + min(cluster2))/2;
    elseif C(2)<C(3) && C(3)<C(1)
        line1 = (max(cluster2) + min(cluster3))/2;
        line2 = (max(cluster3) + min(cluster1))/2;      
    elseif C(3)<C(1) && C(1)<C(2)
        line1 = (max(cluster3) + min(cluster1))/2;
        line2 = (max(cluster1) + min(cluster2))/2;  
    elseif C(3)<C(2) && C(2)<C(1)
        line1 = (max(cluster3) + min(cluster2))/2;
        line2 = (max(cluster2) + min(cluster1))/2;  
    end
    
    plot([line1,line1],[-1,1],'k--','LineWidth',2)
    plot([line2,line2],[-1,1],'k--','LineWidth',2)

    set(gca,'FontSize',20)
    set(gca,'ytick',[])
    txt1 = strcat('k=3');
    text(150,0.008,txt1,'FontSize',20)    
    

    
set(gcf, 'Position', [800, 1000, 1500, 1200])
