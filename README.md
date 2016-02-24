# property_values
<h1>Estimating Property Advertisement Values in the City of Edmonton</h1>


The real estate market is full of opportunities for good financial investments, but it also usually requires a certain degree of domain knowledge and experience. An evidence is the problem of estimation of residential property values: there is no predetermined and objective way to evaluate the financial value of a house or apartment, and because of that, sellers and buyers are forced to rely on the expertise and guidance of professionals (realtors). Previous work in the literature has addressed the problem by applying machine learning techniques, with interesting results, in cities such as Montreal, Canada. However, due to the nature of the problem, the different distribution of properties being sold may cause variations in estimates if the techniques were to be applied in the city of Edmonton. This work presents the results of the application of various regression techniques on a training set containing information about property advertisements in Edmonton, in order to provide estimates of advertisement values of residential properties. 

We show that, amongst the considered methods, support vector regression is the single method that provides best precision in estimates, with mean percentage errors as low as 10.4%, while an ensemble method (bootstrap aggregation) based on SVR, kNN and decision trees yields errors as low as 10.1%. Such results are compatible with related works. The estimates provided may be highly invaluable for standalone sellers, who wish to know how much their properties are worth, and standalone buyers, who do not wish to pay more than what a property is worth.
