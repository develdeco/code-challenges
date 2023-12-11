// Found in GeeksForGeeks
int countVertex(int N, vector<vector<int>>edges){
    vector<vector<int>> vtxMat(N+1,vector<int>(N+1,0));
    vector<set<int>> vtxByEdgeCount(N);
    vector<int> edgeCount(N+1,0);
    set<int> vtxSet;
    
    for(int i=0;i<edges.size();i++){
        int u=edges[i][0],v=edges[i][1];
        edgeCount[u]++;edgeCount[v]++;
        vtxMat[u][v]=1;vtxMat[v][u]=1;
    }
    
    for(int i=1;i<=N;i++){
        vtxByEdgeCount[edgeCount[i]].insert(i);
        vtxSet.insert(i);
    }
    
    int vtxCount=0,edgeCountIdx=N-1;
    while(edgeCountIdx>0 && !vtxSet.empty()){
        set<int> *vtxInEdgeSet=&vtxByEdgeCount[edgeCountIdx];
        set<int>::iterator vtxInEdge=vtxInEdgeSet->begin();
        while(vtxInEdge!=vtxInEdgeSet->end()){
            int vtxInSetBefore=vtxSet.size();
            set<int>::iterator vtx=vtxSet.begin();
            while(edgeCount[*vtxInEdge]>1){
                if(vtxMat[*vtxInEdge][*vtx]>0){
                    vtxByEdgeCount[edgeCount[*vtx]].erase(*vtx);
                    vtxByEdgeCount[edgeCount[*vtx]-1].insert(*vtx);
                    edgeCount[*vtx]--;
                    edgeCount[*vtxInEdge]--;
                    if(edgeCount[*vtx]==0){
                        vtxSet.erase(vtx++);
                    }else{
                        vtx++;
                    }
                }else{
                    vtx++;
                }
            }
            while(vtxMat[*vtxInEdge][*vtx]==0){
                vtx++;
            }
            if(edgeCount[*vtx]==1 || vtxInSetBefore>vtxSet.size()){
                vtxByEdgeCount[edgeCount[*vtx]].erase(*vtx);
                vtxByEdgeCount[edgeCount[*vtx]-1].insert(*vtx);
                vtxByEdgeCount[0].insert(*vtxInEdge);
                edgeCount[*vtx]--;
                edgeCount[*vtxInEdge]=0;
                vtxSet.erase(*vtxInEdge);
                vtxCount++;
                if(edgeCount[*vtx]==0){
                    vtxSet.erase(vtx++);
                }
            }else{
                vtxByEdgeCount[1].insert(*vtxInEdge);
            }
            //vtxInEdgeSet->erase(vtxInEdge++);
            vtxInEdge++;
        }
        edgeCountIdx--;
    }
    
    if(!vtxSet.empty())return 0;
    
    return vtxCount;
}