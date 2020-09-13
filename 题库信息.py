import  os
from typing import NamedTuple,List
from colorUtils import *
class Question(NamedTuple):
	url : str
	source : str
	domain : str

class Source_info(NamedTuple): #每个知识点下面每个题目集合的出处与题目数量信息
	source : str #题目源头名称
	excecise_num : int # 题目数量

class Domain_info(NamedTuple):
	name : str #知识点名称
	sources : List[Source_info] # 每个
	num : int #该板块知识点题目数理
	questions : List[Question]

root = "题库/"
knowledge_domains = os.listdir(root) # 知识点范围
class Bank:
	def __init__(self):
		self.excecises_Bank = []
		for domain in knowledge_domains:
			domain_excecise_sources = os.listdir(root + domain + "/")
			sources = []
			domain_num = 0
			domain_questions = []
			for source in domain_excecise_sources:
				questions_bank = os.listdir(root + domain + "/" + source + "/")
				excecise_num = len(questions_bank)
				questions = []
				for question in questions_bank:
					question_id = int(question.split(".")[0])
					questions.append(Question(url=root + domain + "/" + source + "/" + question,
											  source = source + "第%d题" % question_id,
											  domain = domain))
				sources.append(Source_info(source,excecise_num))
				domain_questions += questions
				domain_num += excecise_num
			self.excecises_Bank.append(Domain_info(domain,sources,domain_num,domain_questions))
	@property
	def total_excecises_num(self):
		num = 0
		for domain in self.excecises_Bank:
			num += domain.num
		return num

	@staticmethod
	def Display_Domain(domain : Domain_info):
		space = "       "
		print("板块:\033[1;31m%s\033[0m(共\033[1;35m%d\033[0m题):" % (domain.name,domain.num))
		for source in domain.sources:
			print(space + "%s : \033[1;33m%d\033[0m(题)" %(source.source,source.excecise_num))
	@staticmethod
	def Display_Domain2(domain : Domain_info):
		space = "       "
		printSkyBlue("板块:%s(共%d题):\n" % (domain.name,domain.num))
		for source in domain.sources:
			print(space + "%s : %d(题)" %(source.source,source.excecise_num))
	def ShowBank(self):
		#下面展示题库
		print("\033[1;30;42m概率论与数理统计题库信息\033[0m")
		print("author : \033[1;34m阿才天下\033[0m wechat: \033[1;34mskydownacai\033[0m")
		print("题库总题量: \033[1;35m%d题\033[0m" % self.total_excecises_num)
		print("Detail :")
		#printWhite("------------概率论与数理统计题库信息-----------\n")
		#printYellow("author : 阿才天下 (wechat : skydownacai) \n")
		for domain in self.excecises_Bank:
			self.Display_Domain(domain)
	def ShowBank2(self):
		printSkyBlue("------------概率论与数理统计题库信息-----------\n")
		printYellow("author : 阿才天下 (wechat : skydownacai) \n")
		printYellow("题库总题量:%d \n" % self.total_excecises_num)
		for domain in self.excecises_Bank:
			self.Display_Domain2(domain)


if __name__ == "__main__":
	bank = Bank()
	bank.ShowBank2()
	os.system("pause")