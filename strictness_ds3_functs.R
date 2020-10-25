## Strictness function code ##

strictness_time <- function(x, y) {
  score <-
    c(rep(0, times = 3), rep(1, times = 7)) # Max score of strictness
  # is 7 out of 10 months
  if (x != "") {
    if (y == "") {
      start_month <- as.numeric(unlist(strsplit(as.character(x), "/"))[1])
      score[1:start_month] <- 0
    } else {
      start_month <- as.numeric(unlist(strsplit(as.character(x), "/"))[1])
      end_month <- as.numeric(unlist(strsplit(as.character(y), "/"))[1])
      score[1:end_month] <- 0
    }
  } else {
    # If x doesn't exist
    if (y == "") {
      #i.e. if both don't exist
      score[1:10] <- 0
    } else {
      score[1:10] <- NA
    }
  }
  score
}

# Reading in data and settting stage for implementation

ds3 <- read.csv("DataSet3.csv")

newds3 <- ds3
newds3 <- newds3[1:562, ] # 562 is last blank county code (i.e. the "state" only data)
strict_states_time <- data.frame(matrix(rep(0, times = 562*10), ncol = 10))
names(strict_states_time) <- paste(month.name[1:10], "_strictness", sep = "")

for (i in seq_len(562)) {
strict_states_time[i, ] <- strictness_time(newds3[i, 6], newds3[i, 7])
}

strict_states_time_cume <- data.frame(matrix(rep(0, times = 51*10), ncol = 10))
names(strict_states_time_cume) <- paste(month.name[1:10], "_strictness", sep = "")


strict_states_time_cume[, 1] <- as.data.frame(newds3 %>%
                                                group_by(state) %>%
                                                summarise(sum(January_strictness,
                                                              na.rm = TRUE)))[,2]
strict_states_time_cume[, 2] <- as.data.frame(newds3 %>%
                                                group_by(state) %>%
                                                summarise(sum(February_strictness,
                                                              na.rm = TRUE)))[,2]
strict_states_time_cume[, 3] <- as.data.frame(newds3 %>%
                                                group_by(state) %>%
                                                summarise(sum(March_strictness,
                                                              na.rm = TRUE)))[,2]
strict_states_time_cume[, 4] <- as.data.frame(newds3 %>%
                                                group_by(state) %>%
                                                summarise(sum(April_strictness,
                                                              na.rm = TRUE)))[,2]
strict_states_time_cume[, 5] <- as.data.frame(newds3 %>%
                                                group_by(state) %>%
                                                summarise(sum(May_strictness,
                                                              na.rm = TRUE)))[,2]
strict_states_time_cume[, 6] <- as.data.frame(newds3 %>%
                                                group_by(state) %>%
                                                summarise(sum(June_strictness,
                                                              na.rm = TRUE)))[,2]
strict_states_time_cume[, 7] <- as.data.frame(newds3 %>%
                                                group_by(state) %>%
                                                summarise(sum(July_strictness,
                                                              na.rm = TRUE)))[,2]
strict_states_time_cume[, 8] <- as.data.frame(newds3 %>%
                                                group_by(state) %>%
                                                summarise(sum(August_strictness,
                                                              na.rm = TRUE)))[,2]
strict_states_time_cume[, 9] <- as.data.frame(newds3 %>%
                                                group_by(state) %>%
                                                summarise(sum(September_strictness,
                                                              na.rm = TRUE)))[,2]
strict_states_time_cume[, 10] <- as.data.frame(newds3 %>%
                                                 group_by(state) %>%
                                                 summarise(sum(October_strictness,
                                                               na.rm = TRUE)))[,2]

sstc_v2 <- cbind(unique(newds3$state), strict_states_time_cume) # to combine state names with strictness score by month
names(sstc_v2)[1] <- "state"
sstc_v2[52, ] <- rep(0, times = 11)
sstc_v2[52, 1] <- "Ohio"
