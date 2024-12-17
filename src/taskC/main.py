import pdb
import glob
import importlib.util
import os
import cv2

path = "../../data/images/C/*"
submission_path = './functions/stitcher.py'  # Path to the single submission
os.makedirs('./results/', exist_ok=True)

try:
    print('****************\tRunning Awesome Stitcher\t********************')
    module_name = 'stitcher_module'
    spec = importlib.util.spec_from_file_location(module_name, submission_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    PanaromaStitcher = getattr(module, 'PanaromaStitcher')
    inst = PanaromaStitcher()

    # Process images in the specified path
    for impaths in glob.glob(path):
        print('\t\t Processing... {}'.format(impaths))
        stitched_image, homography_matrix_list = inst.make_panaroma_for_images_in(path=impaths)

        outfile = './results/{}.png'.format(impaths.split(os.sep)[-1])
        os.makedirs(os.path.dirname(outfile), exist_ok=True)
        cv2.imwrite(outfile, stitched_image)
        print(homography_matrix_list)
        print('Panaroma saved ... @ {}'.format(outfile))
        print('\n\n')

except Exception as e:
    print('Oh No! My implementation encountered this issue\n\t{}'.format(e))
    print('\n\n')
