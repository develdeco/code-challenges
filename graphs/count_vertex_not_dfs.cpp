// Found in GeeksForGeeks
int countVertex(int N, vector<vector<int>>edges){
    vector<int> edgeCount(N+1,0);
    for(int i=0;i<edges.size();i++){
        int u=edges[i][0],v=edges[i][1];
        edgeCount[u]++;edgeCount[v]++;
    }
    
    set<int> vtxSet;
    for(int i=0;i<edges.size();i++){
        int u=edges[i][0],v=edges[i][1];
        if(edgeCount[u]>1 && edgeCount[v]>1){
            edgeCount[u]--;
            edgeCount[v]--;
        }else{
            if(edgeCount[u]==1){
                u=v;
            }
            if(vtxSet.find(u)==vtxSet.end()){
                vtxSet.insert(u);
            }
        }
    }

    return vtxSet.size();
}