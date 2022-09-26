class Path(object):
    @staticmethod
    def db_dir(database):
        if database == 'ucf101':
            # folder that contains class labels
            root_dir = '/Path/to/UCF-101'

            # Save preprocess data into output_dir
            output_dir = '/path/to/VAR/ucf101'

            return root_dir, output_dir
        elif database == 'hmdb51':
            # folder that contains class labels
            root_dir = '/Path/to/hmdb-51'

            output_dir = '/path/to/VAR/hmdb51'

            return root_dir, output_dir
        elif database == 'vehicle_rear_signal':
            # folder that contains class labels
            root_dir = './data/vehicle_rear_signal'

            output_dir = './output/vehicle_rear_signal'

            return root_dir, output_dir

        elif database == 'vehicle_break_signal':
            # folder that contains class labels
            root_dir = './data/vehicle_break_signal'

            output_dir = './output/vehicle_break_signal'

            return root_dir, output_dir
        else:
            print('Database {} not available.'.format(database))
            raise NotImplementedError

    @staticmethod
    def model_dir():
        return './c3d-pretrained/c3d-pretrained.pth'