<h2>Checking-the-authenticity-of-a-national-code-using-mathematics.</h2>
<h4>
  To validate an Iranian National Code (a 10-digit number) using mathematics, a specific algorithm is applied. The last digit is known as the "check digit." The steps are as follows:
</h4><hr>
<li> Take the first 9 digits of the code, one by one from left to right. </li>
  <li> Multiply each of these 9 digits by descending numbers from 10 to 2. For example:<br>
    First digit × 10 <br>
    Second digit × 9 <br>
    ..., and so on, until the ninth digit × 2 
  </li>
  <li> Sum up all the results of these multiplications. </li>
  <li> Divide the sum by 11 and calculate the remainder. </li>
  <li> Check the remainder: </li>
  If the remainder equals the last digit (check digit), the code is valid.<br>
  If the remainder is 1 and the check digit is 0, the code is still considered valid.<br>
  Otherwise, the code is invalid.
  
