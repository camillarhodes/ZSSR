import sys
import os
import configs
import ZSSR


def main(input_img, ground_truth, guiding_img, guiding_img2, kernels, gpu, conf_str, results_path):
    # Choose the wanted GPU
    if gpu is not None:
        os.environ["CUDA_VISIBLE_DEVICES"] = '%s' % gpu

    # 0 input for ground-truth or guiding img or kernels means None
    guiding_img = None if guiding_img == '0' else guiding_img
    guiding_img2 = None if guiding_img2 == '0' else guiding_img2
    ground_truth = None if ground_truth == '0' else ground_truth
    ground_truth = None if ground_truth == '0' else ground_truth
    print('*****', kernels)
    kernels = None if kernels == '0' else kernels.split(';')[:-1]

    # Setup configuration and results directory
    conf = configs.Config()
    if conf_str is not None:
        conf =  getattr(configs, conf_str)
    conf.result_path = results_path

    # Run ZSSR on the image
    net = ZSSR.ZSSR(input_img, conf, ground_truth, guiding_img, guiding_img2, kernels)
    net.run()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
