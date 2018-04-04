import konlpy 
from konlpy.utils import pprint, concordance 
from konlpy.tag import Kkma 
from konlpy.tag import Hannanum
from konlpy import utils

doc = utils.read_txt("corpus/41ListeningText.txt", encoding=u'utf-8');
pprint(doc);

nouns = Hannamun().nouns(doc);
pos = Hannanum().nouns(doc);
cnt = Counter(nouns);


pprint(cnt.most_common(20));
