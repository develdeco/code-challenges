using namespace std;

struct Node{
    int frq;
    char ch;
    Node *left;
    Node *right;
};

class NodeUtil{   
    public:
    static Node* buildNode(int frq,char ch,Node *left,Node *right){
        Node *node=new Node();
        node->frq=frq;
        node->ch=ch;
        node->left=left;
        node->right=right;
        return node;
    }
    static void preOrderVector(Node* node,vector<string> &vec,string code){
        if(node==NULL){
            return;
        }
        if(node->ch!='\0'){
            vec.push_back(code);
        }
        preOrderVector(node->left,vec,code+"0");
        preOrderVector(node->right,vec,code+"1");
    }
};

class NodeComparator
{
    public:
    bool operator() (const Node *a, const Node *b) const
    {
        return a->frq>b->frq;
    }
};

class Solution
{
	public:
	vector<string> huffmanCodes(string S,vector<int> f,int N)
	{
	    priority_queue<Node*,vector<Node*>,NodeComparator> pq;
	    
	    for(int i=0;i<N;i++){
	        pq.push(NodeUtil::buildNode(f[i],S[i],NULL,NULL));
	    }
	    
	    while(pq.size()>1){
	        Node *a=pq.top();pq.pop();
	        Node *b=pq.top();pq.pop();
	        pq.push(NodeUtil::buildNode(a->frq+b->frq,'\0',a,b));
	    }
	    
	    Node *root=pq.top();
	    vector<string> ans;
	    NodeUtil::preOrderVector(root,ans,"");
	    
	    return ans;
	}
};