import sys
from time import sleep
import os
import sys
import version
from urllib.parse import quote

def merge(pdfs):
    
    # buil an empty pdf
    pdf = Pdf.new()

    # loop over each pdf
    for _pdf in pdfs:
        src = Pdf.open(_pdf)
        # add all pages of the open pdf to the new created pdf 
        pdf.pages.extend(src.pages)
        #pdf.save('merged.pdf')
    
    return pdf

def preview(pdf_name):
    
    if pdf_name != "":
        # put in universal format for path 
        pdf_name = pdf_name.replace('\\', '/')
        
        # in case spaces in name we nee dto encode them so that brower does not 
        # split tthe url into several url
        url = "file:///{}".format(quote(pdf_name, safe=":/")) 
        
        os.system("start chrome {}".format(url))

    return pdf_name

def remove_pages(pdf_name, pages):

    pdf = Pdf.open(pdf_name)
    pages_to_be_removed = []
    print(pages)
    print(pdf_name)

    for p in pages.split(','):
        if "-" in p:
            for i in range(int(p.split("-")[0]), int(p.split("-")[1]) + 1):
                pages_to_be_removed.append(i)
        else:
            pages_to_be_removed.append(int(p))

    k = 0
    for p in pages_to_be_removed:

        del pdf.pages[p - 1 - k]
        k += 1

    pdf.save(pdf_name[:-4] + "_pages_removed.pdf")


    return None

class PdfManipulator:


    def __init__(self):

        # initialisation of gui
        self._gui = QtWidgets.QApplication(sys.argv)
        self._MainWindow = QtWidgets.QMainWindow()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self._MainWindow)

        self._MainWindow.setWindowTitle("PDF manipulator")
        
        self.file_logo = "./favicon-32x32.png"
        self._MainWindow.setWindowIcon(QtGui.QIcon(resource_path(self.file_logo)))
        self._MainWindow.setIconSize(QtCore.QSize(200, 200))

        self._MainWindow.show()

        self.pdf_files = None
        
        # do the initialization of gui 
        self.initialize()

        sys.exit(self._gui.exec_())

    def initialize(self):


        self._actions_push_buttons()

        # version
        self._ui.label_version.setText("version: v{}".format(version.__version__))

        # author
        self._ui.label_author.setText("author: {}".format(version.__author__))
        
        # logo
        pixmax = QtGui.QPixmap(resource_path("./logo.png"))
        self._ui.label_logo.setPixmap(pixmax)
        self._ui.label_logo.resize(pixmax.width(), pixmax.height())

        return None

    def _actions_push_buttons(self):
        """ do the connection for all buttons
        """
        self._ui.pushButton_browse.clicked.connect(self._get_files)
        self._ui.pushButton_merge.clicked.connect(self._merge)
        self._ui.pushButton_removeFile.clicked.connect(self._remove_file)
        self._ui.pushButton_preview.clicked.connect(self._preview)
        self._ui.pushButton_removePages.clicked.connect(self._removePagesWindow)

        
        return None

    def _get_selected_pdf(self):

        try:
            index = self._ui.treeWidget_filenames.selectedIndexes()[0]
            _dir = self._ui.treeWidget_filenames.invisibleRootItem().child(index.row()).text(1)
            _filename = self._ui.treeWidget_filenames.invisibleRootItem().child(index.row()).text(2)
            pathname = os.path.join(_dir, _filename)
        except IndexError:
            pathname = ""
    
        return pathname

    def _removePagesWindow(self):

        if self._get_selected_pdf() != "":

            text, ok = QtWidgets.QInputDialog.getText(self._MainWindow, 'Input Dialog', 'Pages ?')

            if ok:
                remove_pages(self._get_selected_pdf(), text)

                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon(resource_path(self.file_logo)))
                msg.setWindowTitle("pdf manipulator message box")
                msg.setText("Votre fichier sans ces pages a été sauvegardé en tant que ./(votre_fichier)_pages_removed.pdf")
                ret = msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                if ret == QtWidgets.QMessageBox.Ok:
                    msg.close()

                msg.exec_()

        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon(resource_path(self.file_logo)))
            msg.setWindowTitle("pdf manipulator message box")
            msg.setText("Veuillez sélectionner un fichier")
            ret = msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            if ret == QtWidgets.QMessageBox.Ok:
                msg.close()

            msg.exec_()

        return None

    def _preview(self):

        pdf_name = preview(self._get_selected_pdf())
        
        if pdf_name == "":
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon(resource_path(self.file_logo)))
            msg.setWindowTitle("pdf manipulator message box")
            msg.setText("Veuillez sélectionner un fichier à visualiser")
            ret = msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            if ret == QtWidgets.QMessageBox.Ok:
                msg.close()
            
            msg.exec_()
        
        return None
    
    def _get_files(self):
        
        self.pdf_files = []
        
        for i, f in enumerate(QtWidgets.QFileDialog.getOpenFileNames()[0]):
            self.pdf_files.append(f)
            
            QtWidgets.QTreeWidgetItem(self._ui.treeWidget_filenames,[str(i + 1),
                                                                     os.path.dirname(f),
                                                                     os.path.basename(f)])
            
        return None
    
    def _update_list(self):
        
        # update list of files to be merged
        self.pdf_files = []
        root = self._ui.treeWidget_filenames.invisibleRootItem()
        
        for i in range(root.childCount()):
            
            self.pdf_files.append(os.path.join(root.child(i).text(1),
                                               root.child(i).text(2)))
                                             
        return None
    
    def _remove_file(self):
        
        root = self._ui.treeWidget_filenames.invisibleRootItem()
        
        for elem in self._ui.treeWidget_filenames.selectedItems():
            (elem.parent() or root).removeChild(elem)
    
        self._update_list()
        
        return None
    
    def _merge(self):
        
        # re arange the list in case move 
        
        self._update_list()
        
        if self.pdf_files == []:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon(resource_path(self.file_logo)))
            msg.setWindowTitle("pdf manipulator message box")
            msg.setText("Veuillez sélectionner au moins 2 fichiers à fusionner")
            ret = msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            if ret == QtWidgets.QMessageBox.Ok:
                msg.close()

            msg.exec_()
        else:
            pdf = merge(self.pdf_files)

            pdf_name = QtWidgets.QFileDialog.getSaveFileName()[0]

            pdf.save(pdf_name)

            sleep(0.5)

            msg = QtWidgets.QMessageBox()

            if os.path.isfile(pdf_name):
                msg.setWindowIcon(QtGui.QIcon(resource_path(self.file_logo)))
                msg.setWindowTitle("pdf manipulator message box")
                msg.setText("Fusion réussie !")
                ret = msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                if ret == QtWidgets.QMessageBox.Ok:
                    msg.close()

                msg.exec_()
        
        return None


if __name__ == "__main__":
    app = PdfManipulator()
