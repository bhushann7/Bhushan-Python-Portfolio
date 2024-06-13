SELECT * FROM apple_products;

SELECT COUNT(*) FROM apple_products;

SELECT AVG(mrp) FROM apple_products;

SELECT MAX(mrp),MIN(mrp) FROM apple_products;

SELECT * FROM apple_products 
	WHERE ram = '4 GB' and star_rating > 4.2 and mrp < 50000;