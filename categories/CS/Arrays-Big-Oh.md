---
export_on_save:
    html: true
title: Arrays and Big O
image: data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPoAAADKCAMAAAC7SK2iAAABxVBMVEX///9ZWVlkgbMAAAD///0AiAAAkwAAjwDg4ODx8eEAigD///n7+PX68/PDw8Pt7e2FhYXz6+X27Oytra2lpaWzs7PS0tLLy8v29va9vb2trUHiw8NCQkLh4cEAoFcjkABVrVXa9fjZwK/p0dHt4tqdnZ0XFxeuSEjy4uK5uWXv793n58xLS0tmZmbBwXrc3LasPz/Ly5GpqTObAABVVVXX367//O3D0peLz7jA5+Tw/P/A3cDQ7OqTvFjPm5vctrbk08erbjylYii3YWGzVVU3rXqo3NG/lXYsLCw1NTXgzb+NjY3IpIrEgYG5iWbS0qK8vG3CmXx2dnb/9tqvz52Zy6FXoxav1rqtx3hcu5VouoKDu2mdv2aDtEdtwaV+sTau3t2Jwo5owaEAoWDb6tupy40AlkFBsYNKpD1MoCu61awnnibl+P8AmDF9uGJEqmuhIiJoqByRNwDIjIyY1ciaypuweEtpqADC4tKenhW7b2+WwX+XUg5rGgBNAABsKgCZiH8/HQCefWWQExMuAABvR0eaXgDKroMaWaCAm8MAGG8AMHhIUnREa6gAPZMAKoymudWmRDS+g3U5OQ+1b1yhMByLa2suORszAAANC0lEQVR4nO2di0PTSB7Hh01JaVNAUAF5iAiVR0UKtQ8QeakVEUStFlB8rVgUVFB3EV3du9vd21vvuXru/b03k6aPNMkkk8wkaelHLW1KJ/ma6e83v5n5zQBQpUqVIoadvgDHOMLVOX0JTsFxNU5fgkMED50+2+r0RThDG6iB/w4oB7W+g6p0G7n1XPwR2rf5vCrYLD16PPszxj+398Qq2Cbd9/3tCQDSSXDOd2sFgNU1u06siV3Sh/g7d709KX4CdPN3+DUQ2p6w6cya2CV9fROAe/dRfe9Oomof4ydZn9IjAutbI/Cp/T/bJf3Bd6iSRy9B6T0gmoHSx1mfMu6vhTwM+deitYn80dij3H+DXdLvfZu/65M23fX4JfFH9LFoWIQNKNkDfCHebuld/sQTfw86r38S3fXCFTAjvokefTz/lOcTIfiYAOmn3me85GTss/Chu48mgSf9EGxNgKEVsLrJ/Ixxfnt7O4Pu+pM1kE6ALu9EehPaW7vvugS8DhGB72F+rvjOBgSdMr6G2hFC93h63Dnp4InUmluxVgyy3HpkK3z2rse8z5F5cVQ6FWJ34Rc4CZ+sJ8XXwgk1wxE/fg4yAW0qNHPpNfDkBRCl5+xrOUoX0pl93xN/EqReSEdU24bRE5Cn411rIJoAQ8/4zCR4OQmElzvS++UoPSrW2dUMuJcA8dtPt1cAqs96KL4i9khvnqZZ2rrosEf4Cdg6Os/vx70TKDYgxhbpgd33NItbF+1XF++rfQ7O34e3vAfdf2LskB4IR/pplhfPoMfVTKx2ApxPgBSSfp+8GDukT03tRmiWN+S9jx4Sgr8nJx2FCKTYUuF7p3oHaJY3wnv5WhgUvEqi252q7RG6TUQEtkhfoioc4tnYR0Y+1zYsPCHBFulhVgWns5GvJ20mArZD+sASlWICC5f7Sg4J2VacZ8NMebaYuQ4KhQSuvX49R6GcAnZIv1hPoxTP3OuTNMrJY4P05gs0Smmaa5o1EK4RYIP0aRqt2JnZACj9plvEBunvm62XcfKa9TJKsUE6hUbs4g3rZShgL733jeUirtG1bxLspS/1WiwgMDtD4zoUsJdutSkHTTuV61DAXLrVphwy7WxgLt1iU46FaZdgLt1afb+xSOkyVGAt3VpTbo+JaZdgLd1KfQ/MzdC6DDVYS7fQnuljZdolGEuvv2j6owt7rEy7BGPp5kMXhqZdgrH0C2ZDl8vGTLtwawXEbmef3yKclMVWuun6btS0x737+Y7o6CWyc7CVbrK+G261C+uPJ1J+ENsPfb9P3DnJVrq5+t43izHtjYePHj4SDAbFF76nL5KrayDqz/zgHwfrZHPxmEo3V991TPtRDtGQfRHfRPU9uj0BXiXyUzENwlT69JSJD+ma9iBUflN6Hr+EhmCQZiQ9Q3QiptLN1Hc90946z8E/uVdQOrrrGeCyu26ivnt0THtLJ9dZ11BI2IHS0XcdSn+bIJ13y1I6eX3XMe11NdyVVgCOBfNHhvYBtPC+FQDOTQIXWXjioQesaQeNN7lTx8Qn8uN5v0445shSOmnosoDrkGm7ynFHVN/Jt+YIB5oZSidtz2BNOzTrVyknKDGU3k8WeeFMO/TlN6lnZrGTTmbfcaa94RQ33Kj5rmnYSZ8iqe+BWc0BNejPzjLJPmUnncTIaXfISP6MBcykDxBMlVvY0xg+zvszFjCT/sb4eNOihmnX9mdUYCbdeH2/pmHaoT8Lqr9DB1bSe42ON3lmF1SPH+a4Q2wzjVlJf29wqlzTnKppx/qzmC/m85m7rGJYSTdY39Vb7Tr+LPTu3bszpq5KBiPpBoM21Q4ZXX/mG3w3Zuqq5DCS3m8oaFMz7dCfcVh/JgwOxsYK9X1ja0UMW25tkKbTsJFubJBRxbS3HeK4w7jPCGfaoeyu/MtX3jsn0ExhGLGSThFmI93IIGNgT2na9fyZZ7Q9JDuwuv0cyvaPo26KuCv64Xf1f6VJ2WrX9WfL7SMlRx6IKQCvEik/NAEGEmCKYSLdgFNXmvZj89xNbHzW1b6sOPZW7KF5kIg/BiiFj+AaGUnXd+qKVnurXnwWah9VaeifRz2Rnu4kquwCYe4PC+n1upNISk173WmuswX3AV/7GUHt+BDKBV89Dtxy13Uj9RLT3jjMzTfgft8H/Zn6Oz8880/G/TvJVC0wlOxWDAvpOi25EtNuwJ8NDmm9t7W11RPa2toH8I7Hne+R1TFyctPeRuzP1IleIu2GZyH9AtbI9c0Vt131/dlYF+7tAo82bhv7xTz0peO7I0/uFb04dkrHn42MKf0ZNehLx7bkFi8XnrfOczV4fzY2SumaVKEvHefZikx7i54/G9LwZ9SgLr1De/p7kWmv0/dn1yn0RmChLl07XC10yKDA9CiuEJw/owZt6QOa4WrBtOt1tBr0Z1ahLV2z+Z437Uf0Bg4N+zOLUJau2XzPJe7oDhyOjJUGpqygLP2NhmeTEnegPxvWi8/oXhAGytLVb7o0TwT6s9PO+jMZdKWrd8RmTTvyZzodrdc14jM20JUeVptNICbutOl2tIr9jXZCVbpqc0Y07S7xZzKoSldrzty4kfVn2A/a5c9k0JSuFqhD067vzxQdrbZAU7rypgf2Zlr0/FlX+zLdvHSjUJTeq5hH0bR37KyuPxu10Z/JoCi9v3QycN+H0/r+zCnhNKUrApeTH3UmwgiDgzb7Mxn0pF+U3/S2Gz/qdLSOtrMPTHFQk17yTQ/+6UesP/Ms2+/IS6AmXfZNP3zq45/x/Y3O+DMZtKQXN+Qa5rkP2NVEulh2tBqGlvRCyNbSyf0Fu4KM+sCh/VCSvpSL0+ugI/8JN7tba+DQfuhIH5CGHRpvcvMNi5jZ3bHrjvozGXSkh0Ublx04xKykYktHq2GoSJ8SeyjEgUMPJnHHgcAUBw3pzcjGZQcOMSup2NffaBAa0sP1aOAQTezUXknFHf5MBgXpb6ZbrmQHDjUTd9ziz2RYl94bHpYGDrVWUhkadIs/k2FZeuPPuYFDjcQdn4v8mQyL0tsOffwlG59p5GQKZxyOz7SxJj3I/SK13TVM++iYq/yZDCvSoT/7q9Q/oZ6Tuew2fybDvHQ0EaZOilpUE3dc6M9kmJXeKvqz/uyQspppd6U/k2FOOozPkD97L8ZrHpVWu0v9mQwz0nMTO6dEE6di2mPO9jcahFw6is/EiTAdoolT5mTaP3BoDmLpV3MTOwdEE7dQ2iHjxMChOQilFybC1O8id6ZotTsycGgOIunFEzvDyLiXmvYRlUQF10IgvfVK0cTOix3KdHv3+zMZhqXLExXeTyvWP7R3IgwFDEovmQizNIUGE4vbrr7BwfISblA6yqAvntg5tVRi2gW3BqY4DEhXZNBPX5C32oWy8Wcy9KUrJnZ2XJSvpLLcXjb+TIaedDQRRj5w2Nsv65BxXUerYfDS0cTOkhFT2IgLFNLtQy4PTHHgpLd0cqdLZwAN7BbN7i4zR16CtnTVDPrm3UJOpq8MAlMcWtLVV4RpDtfnEnfK0p/JUJeusSIMVC6Z9jL1ZzJUpQfVJ3bWh5ulxJ0yis+0UZF+VCPjsD48kM3JHHlXrv5MhkK65oow9eEFMd3e7R2thimRrr0iTHN4EZn2kHMTO2kjkw79WafGxM7m8OXLDk/sxGNkq2I5RdJxK5w1h/cWXe3PUjsjZKvIFknHZtA3736YAe4dOATiDpZm89exGfQDkbm+ZXcOHN5NAuHlOAj5gcl1afAZ9AORWeWKMO4g+gJs9cQz4k72IV5tP25tkPQGfAZ9b+RX13a0PkiAdFLgx9fvA3GDYhJqkD/DZtBD5S7zZ42F+/T2IdqJOm1KeuewToZGR+Rv7hIO+e1T7tt5bw10fxfzTqJFwlOEi7Nwf//HNxg+/fTzP3HvO8O//v2fT9nLD3n9O7x/U1wmnXB5eNCJe1MY/TXCdscdc3zz2++5p5429BegdWleEe7Bjuml8YwOzn5mvOOOKRp/Vx4b2QmRbYeAk77c3rX0tXz6nzYEMtemLR3FZxe+WL0eV6MuXVwRJmxm/44yQk26OHBYH6GxibSbUUrPrnA2ELG6x6jrKZUuJSp0/EFhN2GXI5eemwgzHaayb7i7kUnPdbR+Mb/3XhlRJD2/wtlXglXty5i89PwKZ4HPFe7UckjSCxNhmiI0doovB0TpRSuczVS+U8tRI/qzfEfryUjlO7UcNbLEu0UDiz1XDP8tHjj8eiCcWo6zhaeBz9prI1YiBb9+cEy7RF76ATLtEjnpB8m0S0jSv+y6sROOLVnpB6TVLgdJD/xxQFrtcqD0vorvilKnBvRGDG7HVGkMV1qHTNDwLo9cpRm4Vu6QQfH/G66pMDjuFIPtPcuBI+w2e3Q72FXnq1SpUqVKlSpV3MsG6QyiCiG1/YznCeeDVwgpfxLc+9bpq3AEtE/pOmkGRGVwkKXXHlzpOwDEE05fRZUqVRzi/1RYq+R4D4W2AAAAAElFTkSuQmCC
description: Big O, big theta, big omega and arrays
topics: Asymptotic complexity and arrays 
sources: 
publish: True
---

# Asymptotic Complexity 

## Properties

* Adding Big O - $O(f + g) = O(max(f, g))$
* All are **transitive**
* All are **reflexive**, e.g. $f \in \Omega(f)$
* Only $\Theta$ is **symmetric**, e.g. if $f \in \Theta (g)$, then $g \in \Theta (f)$
* $\Theta$ defines an **equivalence** 

## Function Classification

![Functions](/static/assets/media/functions2.png)

Exponential functions **always** grow **faster** than powers of $n$, so $n^k \in o(c^n)$

## Big $O$ Calculations 

* Consecutive statements - sum of each statement's **max runtime**
* `if` `else` - Time for test plus max of the runtimes 

## Constant 

Input **does not** depend on $n$ 

### Examples

* Getting size of a vector 
* Insertion or removal from a linked list 
* Finding the $k$th element in an array or vector 

## Linear 

Process and perform operation step by step. 

### Examples 

* Printing 
* Finding in arrays, vectors (unsorted) or linked lists (sorted or unsorted)
* Doubling a vector's array 

## Logarithmic 

Running time **cut in half** per iteration 

### Examples 

* Binary search in a sorted array/vector 
* Search in a **balanced tree** 

## Log-Linear 

$\Theta(n \space log(n))$ occurs when you take a linear number of steps, but each one takes $log(n)$ time. 

### Examples 

* Fast sort 
* Quicksort 

## Quadratic 

### Examples 

* Slow sorts, like insertion, bubble and selection 
* Quicksort on a bad day 
* Some graph algorithms 
* Doubly nested loops 

## Exponential

$\Theta(2^n)$, generally trying every solution when there are $2^n$ of them

### Examples

* Binary password cracking
* Traveling salesperson
* Satisfiability of `bool`
