import wikipediaapi

wiki = wikipediaapi.Wikipedia('he')

cats = [wiki.page("קטגוריה:מתמטיקה"),wiki.page("קטגוריה:פיזיקה"),wiki.page("קטגוריה:ספרות"),wiki.page("קטגוריה:דת"),wiki.page("קטגוריה:מוזיקה"),wiki.page("קטגוריה:היסטוריה"),wiki.page("קטגוריה:ישראל"),wiki.page("קטגוריה:פיזיקה"),wiki.page("קטגוריה:כימיה"),wiki.page("קטגוריה:אמנות"),wiki.page("קטגוריה:רפואה"),wiki.page("קטגוריה:ספורט"),wiki.page("קטגוריה:כלכלה")]

f = open("hebrew.txt", "w+")
for cat in cats:
	for c in cat.categorymembers.values():
		for word in c.text.split():
			if word not in f:
				try:
					f.write(word + " ")
				except:
					print()



