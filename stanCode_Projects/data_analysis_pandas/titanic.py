###########################
# import matplotlib       #
# matplotlib.use('TKAgg') #
###########################
import pandas as pd
import matplotlib.pyplot as plt


def main():
	filepath = 'titanic_data/train.csv'
	data = pd.read_csv(filepath)
	print(data)
	print(data.count())
	plt.figure(figsize=(17, 7))
	###
	plt.subplot2grid((3, 4), (0, 0))
	data.Survived.value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Survived')

	plt.subplot2grid((3, 4), (0, 1))
	data.Sex.value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Sex')

	plt.subplot2grid((3, 4), (0, 2))
	data.Pclass.value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Pclass')

	plt.subplot2grid((3, 4), (0, 3))
	data.Age.value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Age')

	plt.subplot2grid((3, 4), (1, 0))
	data.Survived[data.Sex == 'male'].value_counts(normalize=True).sort_index().plot(kind='bar', color='magenta')
	plt.title('Men Survived')

	plt.subplot2grid((3, 4), (1, 1))
	data.Survived[data.Sex == 'female'].value_counts(normalize=True).sort_index().plot(kind='bar', color='red')
	plt.title('Women Survived')

	plt.subplot2grid((3, 4), (1, 2))
	data.Survived[data.Pclass == 1].value_counts(normalize=True).sort_index().plot(kind='bar', color='yellow')
	plt.title('Pclass 1 Survived')

	plt.subplot2grid((3, 4), (1, 3))
	data.Survived[data.Pclass == 3].value_counts(normalize=True).sort_index().plot(kind='bar', color='yellow')
	plt.title('Pclass 3 Survived')

	plt.subplot2grid((3, 4), (2, 0))
	data.Survived[data.Sex == 'male'][data.Pclass == 3].value_counts(normalize=True).sort_index().plot(kind='bar', color='magenta')
	plt.title('Poor Man Survived')

	plt.subplot2grid((3, 4), (2, 1))
	data.Survived[data.Sex == 'male'][data.Pclass == 1].value_counts(normalize=True).sort_index().plot(kind='bar',color='magenta')
	plt.title('Rich Man Survived')

	plt.subplot2grid((3, 4), (2, 2))
	data.Survived[data.Sex == 'female'][data.Pclass == 3].value_counts(normalize=True).sort_index().plot(kind='bar',color='red')
	plt.title('Poor Woman Survived')

	plt.subplot2grid((3, 4), (2, 3))
	data.Survived[data.Sex == 'female'][data.Pclass == 1].value_counts(normalize=True).sort_index().plot(kind='bar',color='red')
	plt.title('Rich Woman Survived',loc='left')

	###
	plt.show()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
