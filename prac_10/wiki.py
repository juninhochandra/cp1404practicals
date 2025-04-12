from wikipedia import wikipedia, PageError, DisambiguationError

PROMPT = "Page title or search phrase: "

title = input(PROMPT)
while title != "":
    try:
        page = wikipedia.page(title)
        print(page.title)
        print(wikipedia.summary(title))
        print(page.url)
    except PageError:
        print(f"Page id \"{title}\" does not match any pages. Try another id!")
    except DisambiguationError:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(wikipedia.suggest(title))
        print(wikipedia.search(title))
    print()
    title = input(PROMPT)

print("Thank you.")
