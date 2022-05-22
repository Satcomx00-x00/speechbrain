from speechbrain.utils.check_yaml import check_yaml_vs_script


def test_yaml_script_consistency(recipe_list="tests/unittests/recipe_list.txt"):
    """This test checks the consistency between yaml files (used to specify
    hyperparameters) and script files (that implement the training recipe).

    Arguments
    ---------
    recipe_list : path
        Path of the a file containing the training scripts with their coupled
        yaml files (every line contains <path_to_training_script> <path_to_yaml_file>)
    """
    check = True
    with open(recipe_list) as f:
        for line in f:
            script_file, hparam_file = (
                line.rstrip().replace(" \n", "\n").replace("  ", " ").split(" ")
            )
            if not (check_yaml_vs_script(hparam_file, script_file)):
                check = False
    assert check
