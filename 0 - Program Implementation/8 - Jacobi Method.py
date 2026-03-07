def jacobi_method(iterations=15):
    x, y, z = 0.0, 0.0, 0.0   # Initial guesses (all zero)

    print(f"{'Iteration':<12} {'x':<10} {'y':<10} {'z':<10}")

    for i in range(1, iterations + 1):
        # Compute ALL new values using OLD values simultaneously
        x1 = (12 - y - z) / 10
        y1 = (13 - 2*x - z) / 10
        z1 = (14 - 2*x - 2*y) / 10

        print(f"{i:<12} {x1:<10.6f} {y1:<10.6f} {z1:<10.6f}")

        # Update ALL at once (this is key to Jacobi!)
        x, y, z = x1, y1, z1

    print(f"\nFinal Answer:  x = {x:.4f},  y = {y:.4f},  z = {z:.4f}")

# Run the method
jacobi_method()
