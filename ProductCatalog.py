import java.util.ArrayList; 
import java.util.Scanner;

interface Operations {
    double calculateDiscount();
    boolean checkAvailability();
}

abstract class Product implements Operations {
    private String name;
    private double price;
    private int stock;

    public Product(String name, double price, int stock) {
        this.name = name;
        this.price = price;
        this.stock = stock; 
    }
    public String getName() { 
        return name; 
    }
    public double getPrice() { 
        return price; 
    }
    public int getStock() { 
        return stock; 
    }

    public void setPrice(double price) {
        this.price = price; 
    }
    public void setStock(int stock) {
        this.stock = stock; 
    }

    @Override
    public boolean checkAvailability() {
        return stock > 0; 
    }
    @Override
    public double calculateDiscount() {
        if (getStock() > 50) {
            return getPrice() * 0.20; } 
            else {
            return 0.0;
        } 
    }
    public abstract String getDetails();
}

class Electronics extends Product {
    private int memoryCapacity;

    public Electronics(String name, double price, int stock, int memoryCapacity) {
        super(name, price, stock);
        this.memoryCapacity = memoryCapacity;
    }
    @Override
    public String getDetails() {
        return "Memory Capacity: " + memoryCapacity + " GB";}
    }

class Clothing extends Product {
    private String size;

    public Clothing(String name, double price, int stock, String size) {
        super(name, price, stock);
        this.size = size;
    }
    @Override
    public String getDetails() {
        return "Size: " + size;
    }
}

class Furniture extends Product {
    private String material;
    public Furniture(String name, double price, int stock, String material) {
        super(name, price, stock);
        this.material = material;
    }
    @Override
    public String getDetails() {
        return "Material: " + material;
    }
}

class ProductCatalog {
    private ArrayList<Product> products = new ArrayList<>();

    public void addProduct(Product product) {
        products.add(product);
    }

    public boolean removeProduct(String name) {
        Product productToRemove = findProduct(name);
        if (productToRemove != null) {
            products.remove(productToRemove);
            return true;
        }
        return false;
    }

    public Product findProduct(String name) {
        for (int i = 0; i < products.size(); i++) {       
            Product p = products.get(i);                  
            if (p.getName().equalsIgnoreCase(name)) {     
                return p; 
                }
            }
                 return null; 
                }

    public void browseProducts() {
        printCategory("Electronics");
        for (Product p : products) {
            if (p.getClass() == Electronics.class) {
                printProduct(p);
                }
            }
        printCategory("Clothing");
        for (Product p : products) {
            if (p.getClass() == Clothing.class) {
                printProduct(p);
                }
            }
        printCategory("Furniture");
        for (Product p : products) {
            if (p.getClass() == Furniture.class) {
                printProduct(p);
            }
        }
    }

    private void printCategory(String category) {
        System.out.println("\n========== " + category.toUpperCase() + " ==========");
    }
        
    private void printProduct(Product product) {
        System.out.println("Name: " + product.getName());
        System.out.printf("Price: $%.2f%n", product.getPrice());
        System.out.println("Stock: " + product.getStock());
        if (product.checkAvailability()) {
            System.out.println("Available: Yes");
        } 
        else {
          System.out.println("Available: No");
        }
        System.out.printf("Discounted Price: $%.2f%n", product.getPrice() - product.calculateDiscount());
        System.out.println(product.getDetails());
        System.out.println();
    }
}

public class OnlineProductCatalog {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean keepRunning = true;

        ProductCatalog catalog = new ProductCatalog();
        catalog.addProduct(new Electronics("Smartphone", 599.99, 25, 256));
        catalog.addProduct(new Clothing("T-Shirt", 29.99, 100, "M"));
        catalog.addProduct(new Furniture("Dining Table", 399.99, 10, "Wood"));

        System.out.println("\n=============== Welcome to Online Product Catalogue! ===============");

        while (keepRunning) {
            System.out.println("--------------------------------------------------------------------");
            System.out.println("Please choose an option below:");
            System.out.println("[1] Browse Products");
            System.out.println("[2] Add New Product");
            System.out.println("[3] Update Existing Product");
            System.out.println("[4] Remove Product");
            System.out.println("[5] Exit Program");
            System.out.print("Enter your choice: ");

            int action = scanner.nextInt();
            scanner.nextLine(); 

            if (action == 1) {
                catalog.browseProducts();
            } else if (action == 2) {
                System.out.print("Enter product type (1: Electronics, 2: Clothing, 3: Furniture): ");
                int type = Integer.parseInt(scanner.nextLine());

                System.out.print("Enter product name: ");
                String name = scanner.nextLine();

                System.out.print("Enter product price: ");
                double price = Double.parseDouble(scanner.nextLine());

                System.out.print("Enter product stock: ");
                int stock = Integer.parseInt(scanner.nextLine());

                if (type == 1) {
                    System.out.print("Enter memory capacity (GB): ");
                    int memory = Integer.parseInt(scanner.nextLine());
                    catalog.addProduct(new Electronics(name, price, stock, memory));
                } else if (type == 2) {
                    System.out.print("Enter size: ");
                    String size = scanner.nextLine();
                    catalog.addProduct(new Clothing(name, price, stock, size));
                } else if (type == 3) {
                    System.out.print("Enter material: ");
                    String material = scanner.nextLine();
                    catalog.addProduct(new Furniture(name, price, stock, material));
                } else {
                    System.out.println("Invalid product type.");
                }
            } else if (action == 3) {
                System.out.print("Enter the product name to update: ");
                String nameToUpdate = scanner.nextLine();

                Product productToUpdate = catalog.findProduct(nameToUpdate);

                if (productToUpdate == null) {
                    System.out.println("Product not found.");
                } else {
                    System.out.printf("Current price: $%.2f%n", productToUpdate.getPrice());
                    System.out.print("Enter new price: ");
                    double newPrice = Double.parseDouble(scanner.nextLine());

                    System.out.printf("Current stock: %d%n", productToUpdate.getStock());
                    System.out.print("Enter new stock: ");
                    int newStock = Integer.parseInt(scanner.nextLine());

                    productToUpdate.setPrice(newPrice);
                    productToUpdate.setStock(newStock);

                    System.out.println("Product updated successfully.");}
                }else if (action == 4) {
                System.out.print("Enter the product name to remove: ");
                String nameToRemove = scanner.nextLine();
                
                if (catalog.removeProduct(nameToRemove)) {
                    System.out.println("Product removed successfully.");
                } else {
                    System.out.println("Product not found.");
                }
            }
            else if (action == 5) {
                keepRunning = false;
                System.out.println("Exiting program. Goodbye!");
            }
            else {
                System.out.println("Invalid option. Please choose between 1 and 5.");
            }
        }
        scanner.close();
    }
}
