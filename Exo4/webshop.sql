CREATE TABLE products( -- crée la table produit
    id SERIAL PRIMARY KEY, -- donne un id unique, une clef primaire
    name VARCHAR(255) NOT NULL, -- défini le nom comme étant un string de max 255 caractere
    price DECIMAL(10,2) NOT NULL, --défini le nombre max de chiffre pouvant etre contenu , le 2 c'est pour les chiffres apres la virgule
    cration_date DATE NOT NULL
);

CREATE TABLE categories(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    is_public BOOLEAN NOT NULL --défini une colonne pour intégrer un boolean pour stocker si c'est public ou non 
);

CREATE TABLE product_categories (
    product_id INT NOT NULL,      
    category_id INT NOT NULL, 
    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE, --si un produit est supp de la table product alors les produist associé seront également supp
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

SELECT p.id, p.name, COUNT(pc.category_id) AS public_category_count --on cible l'id du produit et le nom, on compte combien il y a de catégories associé le AS sert a renommé ce total en colonne public category count pour une meilleur visibilité
FROM products p --la requete commence par products chaque produit sera analysé
JOIN product_categories pc ON p.id = pc.product_id --relie chaque produit a ses associations dans la table pour identifié a quoi appartient chaque produit
JOIN categories c ON pc.category_id = c.id --relie chaque association de produit catégorie a sa catégorie réelle via l'id
WHERE c.is_public = TRUE --seuls les catéhorie public étant true seront incluses
GROUP BY p.id, p.name -- id et nom auront une seule ligne dans le résult
HAVING COUNT(pc.category_id) > 5; --compte combien de catégorie publiques sont associé a chaque produit et filtre le résulte pour ne garder que ceux qui en ont plus de 5