# progeram to calculate Rouge scores
from PyRouge.pyrouge import Rouge

r = Rouge()

system_generated_summary = "Hun Sen's Cambodian People's Party won 64 of the 122 parliamentary seats in July's elections, short of the two-thirds majority needed to form a government on its own.Government and opposition parties have asked King Norodom Sihanouk to host a summit meeting after a series of post-election negotiations between the two opposition groups and Hun Sen's party to form a new government failed.Meanwhile, it says, the old government is holding power illegally.I would like to make it clear that all meetings related to Cambodian affairs must be conducted in the Kingdom of Cambodia,'' Hun Sen told reporters after a Cabinet meeting on Friday.   Cambodian leader Hun Sen on Friday rejected opposition parties' demands for talks outside the country, accusing them oftrying to internationalize'' the political crisis"
manual_summmary = "Cambodian prime minister Hun Sen rejects demands of 2 opposition parties for talks in Beijing after failing to win a 2/3 majority in recent elections.Sihanouk refuses to host talks in Beijing.Opposition parties ask the Asian Development Bank to stop loans to Hun Sen's government.CCP defends Hun Sen to the US Senate.FUNCINPEC refuses to share the presidency.Hun Sen and Ranariddh eventually form a coalition at summit convened by Sihanouk.Hun Sen remains prime minister, Ranariddh is president of the national assembly, and a new senate will be formed.Opposition leader Rainsy left out.He seeks strong assurance of safety should he return to Cambodia."

[precision, recall, f_score] = r.rouge_l([system_generated_summary], [manual_summmary])

print("Precision is :"+str(precision)+"\nRecall is :"+str(recall)+"\nF Score is :"+str(f_score))