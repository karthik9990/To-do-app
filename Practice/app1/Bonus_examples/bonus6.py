contents = ["The rings of Saturn, primarily composed of ice particles with a smaller amount of rocky debris and dust, "
            "are the most extensive planetary ring system of any planet in our solar system",
            "The Great Barrier Reef, located off the coast of Queensland, Australia, is the world’s largest coral "
            "reef system, stretching over 2,300 kilometers",
            "The city of Venice, renowned for its unique setting, architecture, and artwork, is situated on a group "
            "of 118 small islands separated by canals and linked by over 400 bridges"]

filenames = ["saturn.txt", "reef.txt", "venice.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)
