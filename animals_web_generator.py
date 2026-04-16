import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animal_html(animal):
    """ Generates HTML for a single animal """
    characteristics = animal.get("characteristics", {})

    name = animal.get("name", "Unknown")
    diet = characteristics.get("diet", "Unknown")
    location = animal.get("locations", ["Unknown"])[0]
    type_html = ""

    if "type" in characteristics:
        type_html = f"Type: {characteristics['type']}<br>"

    html = f"""
    <li class="cards__item">
        <div class="card__title">{name}</div>
        <p class="card__text">
            Diet: {diet}<br>
            Location: {location}<br>
            {type_html}
        </p>
    </li>
    """

    return html


def load_template(file_path):
    """ Loads HTML template """
    with open(file_path, "r") as file:
        return file.read()


def main():
    animals_data = load_data("animals_data.json")

    animals_html = ""

    for animal in animals_data:
        animals_html += generate_animal_html(animal)

    template = load_template("animals_template.html")

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open("animals.html", "w") as file:
        file.write(final_html)

    print("HTML file successfully generated: animals.html")


if __name__ == "__main__":
    main()