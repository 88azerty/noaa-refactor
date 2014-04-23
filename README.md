noaa-refactor
=============

Modification of the NOAA weather records created by the wview software package to make them more suitable for other climates.

Such a modification is necessary in order to provide more meaningful values under the "days with Highs over 90ºF" and similar summaries, replacing them for "days over 4th quintile, days under 1st quintile", etc. This modification is necessary because the climate of certain regions can have entire months with Highs over the standard value of 90ºF and never reach the Lows under 0ºF. Besides, the use of the Fahrenheit scale is frowned upon in the civilised world :D.

This script aims to recalculate the values generated in the record summaries created by the wview software package (available at http://www.wviewweather.com/) using the text files generated automatically, reparsing the data and counting the days that surpass a given threshold.

Everything in this repository is available under the GNU General Public License v3 (the text of the license is available in the file LICENSE).
