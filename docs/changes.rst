================
Revision history
================

This chapter describes improvements compared to earlier versions of cutplace.

Version 0.4.3, 18-May-2009
==========================

* Fixed auto detection of delimiters in a CSV file, which got broken when
  switching to Python's built in CSV reader with version 0.3.1. See also:
  Ticket #8.

Version 0.4.2, 17-May-2009
==========================

* Added validation for data format property "Allowed characters", which can be
  used with all data formats.

* Added data format property "Header" to specify the number of header rows that
  should be skipped without validation. This property can be used with all data
  formats.

* Added data format property "Sheet" to specify the number of the sheet to
  validate in spreadsheet data formats (Excel and ODS).

* Added complex ranges that consist of several sub ranges separated by a comma
  (,). For example: "10:20, 30:40" means that a value must be between 10 and 20
  or 30 and 40.

* Moved forums to http://apps.sourceforge.net/phpbb/cutplace/.

* Moved project site and issue tracker to
  http://apps.sourceforge.net/trac/cutplace/.

* Fixed handling of data rows with too few or too many items.

* Cleaned up error handling and error messages.

Version 0.4.1, 10-May-2009
==========================

* Added support for Excel and ODS data formats.

Version 0.4.0, 06-May-2009
==========================

* Added support for ICDs stored in Excel format. In order for this to work, the
  xlrd Python package needs to be installed. It is available from
  http://pypi.python.org/pypi/xlrd.

* Changed ICD format: Inserted a new column after the field name and before the
  field type that can contain an optional example value. This enables readers
  to quickly grasp the meaning of a field by taking a glimpse at the first few
  columns instead of having to "decipher" the field type and rule.

Version 0.3.1, 03-May-2009
==========================

* Added proper error messages for several possible error the user might make
  when writing an ICD. So far these errors resulted into confusing messages
  about failed assertions, attempted ``NoneType`` accesses and the like.

* Added requirement that field names in the ICD only use ASCII letters, digits
  and underscore (_). This is necessary to prevent Python errors in checks that
  refer to field values using Python variables, such as DistinctCount and
  IsUnique.

* Changed CSV parser to use Python's built in one. This works around the
  following issues:

  - Improved performance when working with CSV data (about 4 times faster).

  - Error when reading valid CSV data that contained nothing but a single item
    separator.

  However, it also introduces new issues:

  - Increased memory usage when working with CSV data because ``csv.reader``
    does not fit well with the ``AbstractParser`` class. Currently the whole
    file is read into memory.

  - Lack of any error detection in the CSV structure. For example, unclosed
    quotes at the end or inconsistent line feeds do not raise any errors.

* On the long run, cutplace will need its own CSV parser. If only this would
  not be so boring to code...

* Improved error messages for broken field names and types in the ICD.

Version 0.3.0, 28-Apr-2009
==========================

* Fixed error messages in case field name or type was missing in ICD.

* Fixed handling of percent sign (%) in ``DateTime`` field format.

* Changed syntax to specify ranges like field lengths or rules for ``Integer``
  fields formats. Use ":" instead of "...".

* There are basically two reasons for this change: Firstly, this looks more
  Python-like and thus more consistent with other parts of the ICD like the
  "Checks" section which also uses Python syntax in various places. Secondly,
  this avoids issues with Excel which under certain circumstances changes the 3
  characters in "..." to a single character ellipsis. Using ":" still is not
  without issues though: if you use a spreadsheet application to author ICDs,
  most of them think of a value like "1:60" (which could for example specify a
  field length between 1 and 60 characters) to refer to a time of 1 hour and 60
  minutes. To avoid any confusion, disable the cell format auto detection of
  the spreadsheet application by changing all cells to contain "Text".

Version 0.2.2, 07-Apr-2009
==========================

* Added support to use data encodings other than ASCII by specifying them in
  the data format section of the ICD using the encoding property.

* Added support for fixed data format.

* Added command line option ``--browse`` to be used together with ``--web`` in
  order to open the validation page in the web browser.

* Added command line option ``--icd-encoding`` to specify the character encoding
  to be used with ICDs in CSV format.

Version 0.2.1, 29-Mar-2009
==========================

* Added support for ICDs in ODS format for command line client.

* Added ``cutplace.exe`` for Windows, which will be generated during
  installation.

* Added automatic installation of setuptools when you try to build cutplace
  using the Subversion repository. This feature is provided by ``ez_setup.py``,
  which is available from the setuptools site.

* Fixed cutplace script, which did exit with an ``ExitQuietlyOptionError`` for
  options that just showed some information and exited (such as ``--help``).

Version 0.2.0, 27-Mar-2009
==========================

* Added option ``--web`` and ``--port`` to launch web server providing a simple
  graphical user interface for validation.

* Changed ``--listencodings`` to ``--list-encodings``.

Version 0.1.2, 22-Mar-2009
==========================

* Added ``DistinctCount`` check.

* Added ``IsUnique`` check.

* Added command line option ``--trace``.

* Added support to validate an ICD when no data are specified in the command
  line.

* Cleaned up error messages.

Version 0.1.1, 17-Mar-2009
==========================

* Initial release.