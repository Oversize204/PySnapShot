import os
import glob

from PySide2.QtCore import QObject, QAbstractListModel, Qt, QModelIndex, Property, Signal, Slot


class PhotoData(object):
  
  def __init__(self, filename : str):
    self._name = os.path.basename(filename)
    self._full_path_name = os.path.abspath(filename)
    self._rating = 5
    self._date_taken = None
    self._date_modified = None
    self._size = None 

  @property
  def filename(self):
    return self._name

  @property
  def rating(self):
    return self._rating

  @rating.setter
  def rating(self, value):
    self._rating = value

  @property
  def date_taken(self):
    return self._date_taken

    @property
    def date_modified(self):
      return self._date_modified

  @property
  def size(self):
    return self._size

  @property
  def full_path_name(self):
      return self._full_path_name

    
class PhotoModel(QAbstractListModel):

  FileName = Qt.UserRole
  Rating = Qt.UserRole + 1
  DateTaken = Qt.UserRole + 2
  DateModfied = Qt.UserRole + 3
  Size = Qt.UserRole + 4
  FullPathName = Qt.UserRole + 5

  def __init__(self, folder : str, parent : QObject =None):
    super().__init__(parent)
    abspath = os.path.abspath(folder)
    files = glob.glob(os.path.join(folder, "*.jpg"))
    self._photoList = [PhotoData(filename) for filename in files]
    self._currentIndex = 0

  def roleNames(self):
    roles = dict()
    roles[PhotoModel.FileName] = b"fileName"
    roles[PhotoModel.Rating] = b"rating"
    roles[PhotoModel.DateTaken] = b"dateTaken"
    roles[PhotoModel.DateModfied] = b"dateModified"
    roles[PhotoModel.Size] = b"size"
    roles[PhotoModel.FullPathName] = b"fullPathName"
    return roles

  def rowCount(self, parent = QModelIndex()):
    return len(self.self._photoList)

  def data(self, index, role = Qt.DisplayRole):
    if not index.isValid():
      return None

    photo = self._photoList[index.row()]

    if role == PhotoModel.FileName:
      return photo.filename
    elif role == PhotoModel.Rating:
      return photo.rating
    elif role == PhotoModel.DateTaken:
      return photo.date_taken
    elif role == PhotoModel.DateModfied:
      return photo.date_modified
    elif role == PhotoModel.Size:
      return photo.size
    elif role == PhotoModel.FullPathName:
      return photo.full_path_name
    else:
      return None

  def _get_currentFileName(self):
    if not self._photoList:
      return None
    return self._photoList[self._currentIndex].filename

  @Signal
  def _notify_currentFileName(self):
    pass

  currentFileName = Property(str, _get_currentFileName, notify=_notify_currentFileName)

  def _get_currentRating(self):
    if not self._photoList:
      return None
    return self._photoList[self._currentIndex].rating

  def _set_currentRating(self, value):
    if not self._photoList:
      return None
    photoData = self._photoList[self._currentIndex]
    if photoData.rating == value:
      return
    photoData.rating = value
    self._photoList[self._currentIndex] = photoData
    self._notify_currentRating.emit()

  @Signal
  def _notify_currentRating(self):
    pass

  currentRating = Property(int, _get_currentRating, _set_currentRating, notify=_notify_currentRating)
