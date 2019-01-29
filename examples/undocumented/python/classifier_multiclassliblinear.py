#!/usr/bin/env python
from tools.multiclass_shared import prepare_data

[traindat, label_traindat, testdat, label_testdat] = prepare_data(False)

parameter_list = [[traindat,testdat,label_traindat,label_testdat,2.1,1,1e-5],[traindat,testdat,label_traindat,label_testdat,2.2,1,1e-5]]

def classifier_multiclassliblinear (fm_train_real=traindat,fm_test_real=testdat,label_train_multiclass=label_traindat,label_test_multiclass=label_testdat,width=2.1,C=1,epsilon=1e-5):
	from shogun import MulticlassLabels
	import shogun as sg

	feats_train=sg.features(fm_train_real)
	feats_test=sg.features(fm_test_real)

	labels=MulticlassLabels(label_train_multiclass)

	classifier = sg.machine("MulticlassLibLinear", C=C, labels=labels)
	classifier.train(feats_train)

	label_pred = classifier.apply(feats_test)
	out = label_pred.get("labels")

	if label_test_multiclass is not None:
		from shogun import MulticlassAccuracy
		labels_test = MulticlassLabels(label_test_multiclass)
		evaluator = MulticlassAccuracy()
		acc = evaluator.evaluate(label_pred, labels_test)
		print('Accuracy = %.4f' % acc)

	return out

if __name__=='__main__':
	print('MulticlassLibLinear')
	classifier_multiclassliblinear(*parameter_list[0])
