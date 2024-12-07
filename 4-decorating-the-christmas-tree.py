def create_xmas_tree(height, ornament):
    v_tree = ''
    for i in range(height):
        v_tree += f"{'_' * (height - i - 1) + ornament *
                     (2 * i + 1) + '_' * (height - i - 1)}\n"

    v_tree += f"{'_' * (height - 1) + '#' + '_' * (height - 1)}\n"
    v_tree += f"{'_' * (height - 1) + '#' + '_' * (height - 1)}\n"

    return v_tree


tree = create_xmas_tree(6, '@')
print(tree)
