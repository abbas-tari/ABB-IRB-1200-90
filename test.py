import logging
import pyikfast_abb_irb_1200_90
import numpy as np


def check_inverse_kinematics(target_position, initial_orientation):
    try:
        ik_solutions = pyikfast_abb_irb_1200_90.inverse(target_position, initial_orientation)
        logging.info(f'Inverse kinematics solutions: {ik_solutions}')
        return ik_solutions
    except Exception as e:
        logging.error(f'Failed to compute inverse kinematics: {e}')
        return None

def check_forward_kinematics(joint_values):
    try:
        fk_solution = pyikfast_abb_irb_1200_90.forward(joint_values)
        logging.info(f'Forward kinematics solution: {fk_solution}')
        return fk_solution
    except Exception as e:
        logging.error(f'Failed to compute forward kinematics: {e}')
        return None

def main():

    # Constants
    TARGET_POSITION = [0.1, -0.2, 0.2]
    INITIAL_ORIENTATION = [1, 0, 0, 0, 1, 0, 0, 0, 1]
    JOINT_VALUES = [-1.481038152604946, -2.6630596377257882, 2.302093431716746, 1.5390209749486319, 1.4868366305310918, -1.2084953000784067]

    logging.basicConfig(level=logging.INFO)
    
    logging.info('Checking inverse kinematics-- printing all answers...')
    check_inverse_kinematics(TARGET_POSITION, INITIAL_ORIENTATION)
    
    logging.info('Checking if the forward kinematics returns the same 3D target position')
    check_forward_kinematics(JOINT_VALUES)

if __name__ == '__main__':
    main()
