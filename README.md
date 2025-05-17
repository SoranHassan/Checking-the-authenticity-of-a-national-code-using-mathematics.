<h2 align="center">✅ Checking the Authenticity of a National Code Using Mathematics</h2>

<h4>
  To validate an Iranian National Code (a 10-digit number) using mathematics, a specific algorithm is applied.
  The last digit is known as the "check digit." The steps are as follows:
</h4>

<hr>

<ul>
  <li><b>Step 1:</b> Take the first 9 digits of the code, one by one from left to right.</li>

  <li><b>Step 2:</b> Multiply each of these 9 digits by descending numbers from 10 to 2. For example:<br>
    <code>First digit × 10</code> <br>
    <code>Second digit × 9</code> <br>
    ..., and so on, until <code>ninth digit × 2</code>.
  </li>

  <li><b>Step 3:</b> Sum up all the results of these multiplications.</li>

  <li><b>Step 4:</b> Divide the sum by 11 and calculate the remainder.</li>

  <li><b>Step 5:</b> Check the remainder:</li>
  <ul>
    <li>If the remainder equals the last digit (check digit), the code is <b>valid</b>.</li>
    <li>If the remainder is <code>1</code> and the check digit is <code>0</code>, the code is still considered <b>valid</b>.</li>
    <li>Otherwise, the code is <b>invalid</b>.</li>
  </ul>
</ul>
