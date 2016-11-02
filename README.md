# homesearch

Matt Miller, Oct 2016

Identifying areas with high homeless population using Google Street View Images

This is a project (in development) to identify areas of where there is a high homeless population.

It does the following:

- Searches through an index of addresses (from OpenAddresses database: https://openaddresses.io/)
- Uses those addresses to pull images from Google Street View API (https://developers.google.com/maps/documentation/streetview/)
- Neural network to classify images as containing or not containing evidence of homelessness at that address.
