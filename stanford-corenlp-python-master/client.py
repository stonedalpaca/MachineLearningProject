import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint

class StanfordNLP:
    def __init__(self):
        self.server = ServerProxy(JsonRpc20(),
                                  TransportTcpIp(addr=("127.0.0.1", 8080)))
    
    def parse(self, text):
        return json.loads(self.server.parse(text))

nlp = StanfordNLP()


result = nlp.parse("Curdie saw that something must be done.  He spoke to his father and the rest of the miners, and they at once proceeded to make another outlet for the waters.  By setting all hands to the work, tunnelling here and building there, they soon succeeded; and having also made a little tunnel to drain the water away from under the king's house, they were soon able to get into the wine cellar, where they found a multitude of dead goblins among the rest the queen, with the skin shoe gone, and the stone one fast to her ankle for the water had swept away the barricade, which prevented the men at arms from following the goblins.")#, and had greatly widened the passage.  They built it securely up, and then went back to their labours in the mine.")

pprint(result)
#from nltk.tree import Tree
#tree = Tree.parse(result['sentences'][0]['parsetree'])
#pprint(tree)
