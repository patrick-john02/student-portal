<script lang="ts">
export const description = "Grade reports page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbList,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
} from "@/components/ui/dropdown-menu"

import {
  MoreHorizontal,
  Award,
  Users,
  ChevronRight,
  Printer,
  FileDown,
} from "lucide-vue-next"

const userRole = "Admin"

// Dummy grade report data
const gradeReports = ref([
  {
    id: 1,
    student: "John Mark Rivera",
    gradeLevel: "Grade 11",
    section: "STEM A",
    average: 92.5,
    status: "Passed",
    color: "bg-green-500",
  },
  {
    id: 2,
    student: "Andrea Lopez",
    gradeLevel: "Grade 11",
    section: "HUMSS B",
    average: 84.0,
    status: "Passed",
    color: "bg-blue-500",
  },
    {
    id: 3,
    student: "Rico Delos Santos",
    gradeLevel: "Grade 12",
    section: "ABM A",
    average: 89.3,
    status: "Passed",
    color: "bg-yellow-500",
  },
  {
    id: 4,
    student: "Kyla Francisco",
    gradeLevel: "Grade 12",
    section: "GAS C",
    average: 71.2,
    status: "Failed",
    color: "bg-red-500",
  },
])

const search = ref("")
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4 transition-all">
        <SidebarTrigger class="-ml-2" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/admin/dashboard">Reports</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Grade Reports</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">

        <!-- Top Section -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Grade Reports</h2>
            <p class="text-sm text-muted-foreground">
              View academic performance and grade summaries.
            </p>
          </div>

          <div class="flex gap-2">
            <Button variant="secondary" class="flex items-center gap-2">
              <Printer class="h-4 w-4" />
              Print
            </Button>
            <Button class="flex items-center gap-2">
              <FileDown class="h-4 w-4" />
              Download
            </Button>
          </div>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Students Performance</CardTitle>
            <CardDescription>
              Academic summary per student for the current school year.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <!-- Search -->
            <div class="flex items-center justify-between mb-4">
              <Input
                v-model="search"
                placeholder="Search students..."
                class="max-w-xs"
              />
            </div>

            <!-- Grade Reports Table -->
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-64">Student</TableHead>
                  <TableHead>Grade Level</TableHead>
                  <TableHead>Section</TableHead>
                  <TableHead>Average</TableHead>
                  <TableHead>Status</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="gr in gradeReports"
                  :key="gr.id"
                  class="hover:bg-muted/50"
                >
                  <!-- Student -->
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <Award class="h-4 w-4 text-muted-foreground" />
                      <span class="font-medium">{{ gr.student }}</span>
                    </div>
                  </TableCell>

                  <!-- Grade Level -->
                  <TableCell class="text-muted-foreground">
                    {{ gr.gradeLevel }}
                  </TableCell>

                  <!-- Section -->
                  <TableCell class="flex items-center gap-1">
                    <Users class="h-4 w-4 text-muted-foreground" />
                    <span>{{ gr.section }}</span>
                  </TableCell>

                  <!-- Average -->
                  <TableCell>
                    <span class="font-medium">
                      {{ gr.average.toFixed(1) }}%
                    </span>
                  </TableCell>

                  <!-- Status -->
                  <TableCell>
                    <Badge
                      :variant="gr.status === 'Passed' ? 'default' : 'destructive'"
                    >
                      {{ gr.status }}
                    </Badge>
                  </TableCell>

                  <!-- Actions -->
                  <TableCell class="text-right">
                    <DropdownMenu>
                      <DropdownMenuTrigger as-child>
                        <Button variant="ghost" size="icon">
                          <MoreHorizontal class="h-4 w-4" />
                        </Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent align="end">
                        <DropdownMenuLabel>Actions</DropdownMenuLabel>
                        <DropdownMenuSeparator />

                        <DropdownMenuItem>View Full Report</DropdownMenuItem>
                        <DropdownMenuItem>Print Individual</DropdownMenuItem>
                        <DropdownMenuItem>Download PDF</DropdownMenuItem>

                        <DropdownMenuSeparator />

                        <DropdownMenuItem class="text-red-600">
                          Flag for Review
                        </DropdownMenuItem>
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </TableCell>

                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>

      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
