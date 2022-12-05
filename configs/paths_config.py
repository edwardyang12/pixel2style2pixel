dataset_paths = {
	'celeba_train': '',
	'celeba_test': '',
	'celeba_train_sketch': '',
	'celeba_test_sketch': '',
	'celeba_train_segmentation': '',
	'celeba_test_segmentation': '',
	'ffhq': '',
	'edward_train': '/edward-slow-vol/Sketch2Model/Sketch2Model/data/chair.csv',
	'edward_test': '/edward-slow-vol/Sketch2Model/Sketch2Model/data/chair_test.csv',
	'edward_train_sketch': '/edward-slow-vol/Sketch2Model/Sketch2Model/data/chair_sketch.csv',
	'edward_test_sketch': '/edward-slow-vol/Sketch2Model/Sketch2Model/data/chair_sketch_test.csv',
}

model_paths = {
	'stylegan_ffhq': 'pretrained_models/stylegan2-ffhq-config-f.pt',
	'ir_se50': 'pretrained_models/model_ir_se50.pth',
	'circular_face': 'pretrained_models/CurricularFace_Backbone.pth',
	'mtcnn_pnet': 'pretrained_models/mtcnn/pnet.npy',
	'mtcnn_rnet': 'pretrained_models/mtcnn/rnet.npy',
	'mtcnn_onet': 'pretrained_models/mtcnn/onet.npy',
	'shape_predictor': 'shape_predictor_68_face_landmarks.dat',
	'moco': 'pretrained_models/moco_v2_800ep_pretrain.pt',
	'edward_stylegan': 'pretrained_models/chair_090000.pt',
}
