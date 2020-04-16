import sklearn.metrics as metrics

def plot_confusion_matrix(cm, classes=None, normalize=False,cmap=None,
                          title='Confusion Matrix',title_font={'size':14},
                          annot_kws={'size':10,'weight':50}, 
                          axislabel_font={'size':14,'weight':70}, 
                          tick_font={'size':12,'weight':50},x_rot =45, y_rot=0,
                         fig_kws={'figsize':(5,5)}):
    """ Plots a confusion matrix of either a pre-calculated cm or a tuple of (y_true,y_pred) as cm.
    
    Args:
        cm (array or tuple): Either a confusion amtrix from sklearn or (y_true,y_pred) tuple
        classes (list, optional): Names of classes to use. Defaults to integers 0 to len(cm).
        normalize (bool, optional): Annotate class-percentages instead of counts. Defaults to False.
        cmap (cmap, optional): colormap to use Defaults to plt.get_cmap("Blues").
        title (str, optional): Plot title. Defaults to 'Confusion Matrix'.
        title_font (dict, optional): fontdict for set_title. Defaults to {'size':14}.
        annot_kws (dict, optional): kws for ax.Text annotations. Defaults to {'size':10,'weight':50}.
        axislabel_font (dict, optional): fontdict for ylabel,xlabel. Defaults to {'size':14,'weight':70}.
        tick_font (dict, optional): kws for plt.xticks/yticks. Defaults to {'size':12,'weight':50}.
        x_rot (int, optional): Rotation of x-axis tick labels. Defaults to 45.
        y_rot (int, optional): Rotation of y-axis tick labels.Defaults to 0.
        fig_kws (dict, optional): kws for plt.subplots. Defaults to {}.
    
    Returns:
        fig,ax: matplotlib Figure & Axes
    """
    import itertools
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    import sklearn.metrics as metrics
    
    ## If (y_true,y_pred) passed as cm
    if isinstance(cm, tuple):
        cm = metrics.confusion_matrix(*cm)
        
    ## if normalize:  normalize counts to class-accuracy
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        

    
    ## Setting & updating default kws
    subplots_kws = {}
    subplots_kws.update(fig_kws)
    
    ## Annotation kws
    text_kws = dict(horizontalalignment="center")
    text_kws.update(annot_kws)    
    
    ## Axis Labels
    axlabel_kws = dict(size=12, weight='bold')
    axlabel_kws.update(axislabel_font)
    
    ## Tick Labels
    ticklabel_kws = dict(size=10)
    ticklabel_kws.update(tick_font)
    

    ## Define classes if not 
    if classes is None:
        classes = list(range(len(cm)))
        
    ## Default cmap
    if cmap is None:
        cmap = plt.get_cmap("Blues")



    ## Create fig,ax and plot iamge
    fig, ax = plt.subplots(**subplots_kws)
    
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.set_title(title,fontdict=title_font)

    
    ## Create Ticks
    tick_marks = np.arange(len(classes))
    
    plt.xticks(tick_marks, classes, rotation=x_rot,**ticklabel_kws)
    plt.yticks(tick_marks, classes, rotation=y_rot,**ticklabel_kws)

    ## Set annotation fmt and color threshold
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    
    ## Add cm labels
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        # text_kws.update(color=color)
        ax.text(j, i, format(cm[i, j], fmt),color="white" if cm[i, j] > thresh else "black",fontdict=text_kws)
                
    ## Set axis labels
    ax.set_ylabel('True Label',fontdict=axislabel_font)
    ax.set_xlabel('Predicted Label',fontdict=axislabel_font)
     
    ## Add colorbar
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)
    fig.colorbar(im,cax=cax)     

#     plt.tight_layout()

    return fig,ax



def plot_auc_roc_curve(y_test, y_test_pred,figsize=(8,4)):
    """ Takes y_test and y_test_pred from a ML model and uses sklearn roc_curve to plot the AUC-ROC curve."""
    from sklearn.metrics import roc_curve, auc, roc_auc_score
    import matplotlib.pyplot as plt
    
    assert y_test.shape==y_test_pred.shape
    auc = roc_auc_score(y_test, y_test_pred)#[:,1])

    FPr, TPr, _  = roc_curve(y_test, y_test_pred)#[:,1])
#     auc()
    fig,ax=plt.subplots(figsize=figsize)
    ax.plot(FPr, TPr,label=f"AUC for Classifier:\n{round(auc,2)}" )

    ax.plot([0, 1], [0, 1],  lw=2,linestyle='--')
    ax.set_xlim([-0.01, 1.0])
    ax.set_ylim([0.0, 1.05])

    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax.set_title('Receiver Operating Characteristic (ROC) Curve')
    ax.legend(loc="lower right")
#     plt.show()
    return fig, ax


def plot_importance(tree, top_n=20,figsize=(10,10)):
    df_importance = pd.Series(tree.feature_importances_,index=X_train.columns)
    df_importance.sort_values(ascending=True).tail(top_n).plot(
        kind='barh',figsize=figsize)
    return df_importance


## Write a fucntion to evalute the model
def evaluate_model(y_test, y_hat_test,tree=None,
                   conf_matrix_kws={'normalize':True},
                   roc_curve_kws ={}):
    print(metrics.classification_report(y_test, y_hat_test))
    
    if tree is None:
        df_important=None
    try: 
        df_important = plot_importance(tree)
    except:
        df_important = None
    
    fig, ax = plot_confusion_matrix((y_test,y_hat_test),**conf_matrix_kws)
    fig2, ax2 = plot_auc_roc_curve(y_test,y_hat_test)
#     return df_important


## visualize the decision tree
def visualize_tree(tree,feature_names=None,class_names=['0','1'],export_graphviz_kws={}):
    """Visualizes a sklearn tree using sklearn.tree.export_graphviz"""
    from sklearn.tree import export_graphviz
    from IPython.display import SVG
    from graphviz import Source
    from IPython.display import display
    if feature_names is None:
        feature_names=X_train.columns

    tree_viz_kws =  dict(out_file=None, rotate=False, filled = True)
    tree_viz_kws.update(export_graphviz_kws)

    # tree.export_graphviz(dt) #if you wish to save the output to a dot file instead
    graph = Source(export_graphviz(tree,feature_names=feature_names, class_names=class_names,**tree_viz_kws))
    display(SVG(graph.pipe(format='svg')))
    
    
class Timer():
    def __init__(self, start=True,time_fmt='%m/%d/%y - %T'):
        import tzlocal
        import datetime as dt
        
        self.tz = tzlocal.get_localzone()
        self.fmt= time_fmt
        self._created = dt.datetime.now(tz=self.tz)
        
        if start:
            self.start()
            
    def get_time(self):
        import datetime as dt
        return dt.datetime.now(tz=self.tz)

        
    def start(self,verbose=True):
        self._laps_completed = 0
        self.start = self.get_time()
        if verbose: 
            print(f'[i] Timer started at {self.start.strftime(self.fmt)}')
    
    def stop(self, verbose=True):
        self._laps_completed += 1
        self.end = self.get_time()
        self.elapsed = self.end -  self.start
        if verbose: 
            print(f'[i] Timer stopped at {self.end.strftime(self.fmt)}')
            print(f'  - Total Time: {self.elapsed}')