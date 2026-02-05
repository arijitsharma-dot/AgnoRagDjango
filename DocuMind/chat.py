from rag import DocuMindRAG

def main():
    bot = DocuMindRAG()

    print("📘 DocuMind is ready. Ask your PDF.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("🧑 You: ")

        if query.lower() == "exit":
            break

        chunks = bot.retrieve(query)
        answer, pages = bot.generate_answer(query, chunks)

        print("\n🤖 DocuMind:")
        print(answer)

        if pages:
            print(f"\n📄 Source pages: {pages}")
        print("-" * 50)


if __name__ == "__main__":
    main()
