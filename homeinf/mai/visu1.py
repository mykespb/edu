# Функция для визуализации дерева
def visualize_tree(model, feature_names, class_names):
    plt.figure(figsize=(10, 6))
    plot_tree(model, feature_names=feature_names, class_names=class_names, filled=True)
    plt.title("Решающее дерево")
    plt.show()