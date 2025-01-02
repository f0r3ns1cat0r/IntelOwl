import axios from "axios";

import { addToast } from "@certego/certego-ui";
import { PLUGIN_REPORT_QUERIES } from "../../constants/apiURLs";
import { prettifyErrors } from "../../utils/api";

export async function pluginReportQueries(body, pageSize, pageLimit) {
  let resultList = [];
  const params = body;
  // default request: page=1
  params.page = 1;
  params.page_size = pageSize;
  try {
    const resp = await axios.get(PLUGIN_REPORT_QUERIES, { params });
    resultList = resultList.concat(resp.data.results);
    // in case there are others pages, download all of them concurrently
    if (resp.data.total_pages > 1) {
      const additionalRequests = [];
      for (
        let addtionalPageIndex = 2;
        // in case there are too many data don't download all of them
        addtionalPageIndex <= Math.min(resp.data.total_pages, pageLimit);
        addtionalPageIndex += 1
      ) {
        params.page = addtionalPageIndex;
        params.page_size = pageSize;
        additionalRequests.push(axios.get(PLUGIN_REPORT_QUERIES, { params }));
      }
      const multipleResponses = await Promise.all(additionalRequests);
      multipleResponses.forEach((response) => {
        resultList = resultList.concat(response.data.results);
      });
    }
    return resultList;
  } catch (error) {
    addToast("Query failed!", prettifyErrors(error), "danger", true);
    return Promise.reject(error);
  }
}