def generate_animal_html(animal):
    characteristics = animal.get("characteristics", {})

    name = animal.get("name", "Unknown")
    diet = characteristics.get("diet", "Unknown")
    location = animal.get("locations", ["Unknown"])[0]

    type_html = ""
    if "type" in characteristics:
        type_html = f"<li><strong>Type:</strong> {characteristics['type']}</li>"

    html = f"""
    <li class="cards__item">
        <div class="card__title">{name}</div>
        <div class="card__text">
            <ul class="animal-details">
                <li><strong>Diet:</strong> {diet}</li>
                <li><strong>Location:</strong> {location}</li>
                {type_html}
            </ul>
        </div>
    </li>
    """

    return html