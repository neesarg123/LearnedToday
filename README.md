## GOAL: 
This purpose of this project is two-fold:
1. Serve as a place where I can note down important things I learn everyday.
2. Compile a dataset which **maps textual statements to abstract ideas/concepts** (much like topic modeling). 

### Building on Purpose #2: Potential Uses of the Dataset
1. Perform time-series analytics on user's learning journey.
2. Create knowledge graphs using text mapped to a wide range of interdisciplinary topics/classes.
3. Enable both supervised and unsupervised topic modeling.
4. Fine-tune pretrained models (such as BERT) on topic-specific data. 

### Scaling
In order to create a highly useable dataset there are two primary obstacles to overcome due to the nature of this project:
1. Redundancy/duplication of similar topics (e.g. "Math" and "Mathematics")
     * Enforcement of a limit in topic length and automated reallocation of topic words will need to be implemented.
2. Open the database for read and write access to the wider public for augmenting dataset size to a useable amount. 
     * Note that obstacle #1 will need to be addressed ahead of time. 
     * Additional constraints on user inputs will need to addressed here as well. 
     
#### Daily Updated Database
[today](https://witty-pump-eda.notion.site/c9060f07a02f40b7b29d3d0efdc6b40f?v=f9aacc7b973b487a999b1d3771a80b1d)
