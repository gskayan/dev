## Copyright (C) 2018 Gleb Skaianski
## 
## This program is free software; you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

## -*- texinfo -*- 
## @deftypefn {} {@var{retval} =} createOutput (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Gleb Skaianski <gskaian@ip-1-70-93-109>
## Created: 2018-09-28

createOutput is the command-line function:

function y = createOutput (input, theta)
  y = zeros (length (input), 1);
  for i = 1:length (y)
	    y (i) = theta + (theta+1) * input (i) + (theta+2) * input (i) ^ (theta+1) + (theta+3) * input (i) ^ (theta+2);
  endfor
endfunction

