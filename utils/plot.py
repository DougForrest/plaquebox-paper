from sklearn.metrics import roc_curve, auc, precision_recall_curve
from matplotlib import pyplot as plt


def roc(preds, label, image_classes, size=20, path=None, dataset=None, model_name=None):
    colors = ['pink','c','deeppink', 'b', 'g', 'm', 'y', 'r', 'k']
    fig = plt.figure(figsize=(1.2*size, size))
    ax = plt.axes()
    output = {}
    for i in range(preds.shape[1]):
        class_name = image_classes[i]
#         output[class_name] = {}
        fpr, tpr, _ = roc_curve(label[:,i].ravel(), preds[:,i].ravel())
        output[f"AUROC_#{class_name}"] = auc(fpr, tpr)

        lw = 0.2*size
        # Plot all ROC curves
        ax.plot([0, 1], [0, 1], 'k--', lw=lw, label='random')
        ax.plot(fpr, tpr,
                 label='ROC-curve of {}'.format(class_name)+ '( area = {0:0.3f})'
                ''.format(output[f"AUROC_#{class_name}"]),
                  color=colors[(i+preds.shape[1])%len(colors)], linewidth=lw)
       
    
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('False Positive Rate', fontsize=1.8*size)
    ax.set_ylabel('True Positive Rate', fontsize=1.8*size)
    ax.set_title(f'Receiver operating characteristic Curve\nfor {model_name} on {dataset} data', fontsize=1.8*size, y=1.01)
    ax.legend(loc=0, fontsize=1.5*size)
    ax.xaxis.set_tick_params(labelsize=1.6*size, size=size/2, width=0.2*size)
    ax.yaxis.set_tick_params(labelsize=1.6*size, size=size/2, width=0.2*size)
    
    if path != None:
        fig.savefig(path)
#         plt.close(fig)
        print('saved')

    return(output)
    
def prc(preds, label, image_classes, size=20, path=None, dataset=None, model_name=None):
    colors = ['pink','c','deeppink', 'b', 'g', 'm', 'y', 'r', 'k']
    
    fig = plt.figure(figsize=(1.2*size,size))
    ax = plt.axes()
    output = {}
    for i in range(preds.shape[1]):
        rp = (label[:,i]>0).sum()/len(label)
        precision, recall, _ = precision_recall_curve(label[:,i].ravel(), preds[:,i].ravel())
        class_name = image_classes[i]
#         output[class_name] = {}
        output[f"AUPRC_#{class_name}"] = auc(recall, precision)
        lw=0.2*size
    
        ax.plot(recall, precision,
                 label='PR-curve of {}'.format(class_name)+ '( area = {0:0.3f})'
                ''.format(output[f"AUPRC_#{class_name}"]),
                 color=colors[(i+preds.shape[1])%len(colors)], linewidth=lw)

        ax.plot([0, 1], [rp, rp], 'k--', color=colors[(i+preds.shape[1])%len(colors)], lw=lw, label='random')
   
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('Recall', fontsize=1.8*size)
    ax.set_ylabel('Precision', fontsize=1.8*size)
    ax.set_title(f'Precision-Recall curve\nfor {model_name} on {dataset} data', fontsize=1.8*size, y=1.01)
    ax.legend(loc="lower left", bbox_to_anchor=(0.01, 0.1), fontsize=1.5*size)
    ax.xaxis.set_tick_params(labelsize=1.6*size, size=size/2, width=0.2*size)
    ax.yaxis.set_tick_params(labelsize=1.6*size, size=size/2, width=0.2*size)
    
    if path != None:
        fig.savefig(path)
#         plt.close(fig)
        print('saved')
    return(output)